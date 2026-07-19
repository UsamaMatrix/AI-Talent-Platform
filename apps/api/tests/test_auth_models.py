"""Unit tests for authentication domain models and schemas."""

import uuid
from datetime import datetime

import pytest

from src.api.v1.schemas.auth import (
    AuditLogRead,
    MembershipRead,
    OrganizationCreate,
    OrganizationRead,
    PermissionRead,
    RoleCreate,
    RoleRead,
    UserCreate,
    UserRead,
)
from src.domain.models.auth import (
    AuditLog,
    Membership,
    Organization,
    Permission,
    RefreshToken,
    Role,
    RolePermission,
    User,
)


def _uuid() -> uuid.UUID:
    return uuid.uuid4()


def _now() -> datetime:
    return datetime.utcnow()


class TestOrganizationModel:
    def test_defaults(self) -> None:
        org = Organization(name="Acme", slug="acme", is_active=True)
        assert org.is_active is True
        assert org.deleted_at is None

    def test_slug_stored(self) -> None:
        org = Organization(name="Test Co", slug="test-co")
        assert org.slug == "test-co"


class TestUserModel:
    def test_defaults(self) -> None:
        user = User(
            email="user@example.com",
            normalized_email="user@example.com",
            full_name="Test User",
            is_active=True,
            is_superuser=False,
            email_verified=False,
        )
        assert user.is_active is True
        assert user.is_superuser is False
        assert user.email_verified is False
        assert user.password_hash is None
        assert user.deleted_at is None

    def test_email_stored(self) -> None:
        user = User(
            email="Admin@Example.com",
            normalized_email="admin@example.com",
            full_name="Admin",
        )
        assert user.email == "Admin@Example.com"
        assert user.normalized_email == "admin@example.com"


class TestRoleModel:
    def test_defaults(self) -> None:
        role = Role(organization_id=_uuid(), name="admin", is_system=False)
        assert role.description is None
        assert role.is_system is False

    def test_system_role(self) -> None:
        role = Role(organization_id=_uuid(), name="owner", is_system=True)
        assert role.is_system is True


class TestPermissionModel:
    def test_fields(self) -> None:
        perm = Permission(code="resume.read", description="Read resumes")
        assert perm.code == "resume.read"
        assert perm.description == "Read resumes"


class TestRolePermissionModel:
    def test_fields(self) -> None:
        rp = RolePermission(role_id=_uuid(), permission_id=_uuid())
        assert rp.role_id is not None
        assert rp.permission_id is not None


class TestMembershipModel:
    def test_defaults(self) -> None:
        m = Membership(user_id=_uuid(), organization_id=_uuid(), role_id=_uuid(), is_active=True)
        assert m.is_active is True


class TestRefreshTokenModel:
    def test_fields(self) -> None:
        token = RefreshToken(
            user_id=_uuid(),
            token_hash="sha256:abc123",  # noqa: S106
            expires_at=_now(),
        )
        assert token.revoked_at is None
        assert token.replaced_by_id is None
        assert token.token_hash == "sha256:abc123"  # noqa: S105


class TestAuditLogModel:
    def test_fields(self) -> None:
        log = AuditLog(action="user.created", target_type="user")
        assert log.actor_id is None
        assert log.correlation_id is None
        assert log.event_metadata is None

    def test_target_fields(self) -> None:
        tid = str(_uuid())
        log = AuditLog(
            action="org.updated",
            target_type="organization",
            target_id=tid,
            correlation_id="corr-123",
        )
        assert log.target_id == tid
        assert log.correlation_id == "corr-123"


class TestOrganizationSchemas:
    def test_create_valid(self) -> None:
        org = OrganizationCreate(name="Acme Corp", slug="acme-corp")
        assert org.slug == "acme-corp"

    def test_create_invalid_slug(self) -> None:
        import pydantic

        with pytest.raises(pydantic.ValidationError, match="slug"):
            OrganizationCreate(name="Bad Slug", slug="Bad Slug!")

    def test_read_from_attributes(self) -> None:
        org = Organization(id=_uuid(), name="Acme", slug="acme", is_active=True, created_at=_now())
        read = OrganizationRead.model_validate(org)
        assert read.slug == "acme"


class TestUserSchemas:
    def test_create_valid(self) -> None:
        u = UserCreate(email="user@example.com", full_name="Test User", organization_id=_uuid())
        assert u.email == "user@example.com"

    def test_read_from_attributes(self) -> None:
        user = User(
            id=_uuid(),
            email="user@example.com",
            normalized_email="user@example.com",
            full_name="Test",
            is_active=True,
            email_verified=False,
            created_at=_now(),
        )
        read = UserRead.model_validate(user)
        assert read.email == "user@example.com"


class TestPermissionSchemas:
    def test_read_from_attributes(self) -> None:
        perm = Permission(
            id=_uuid(), code="resume.read", description="Read resumes", created_at=_now()
        )
        read = PermissionRead.model_validate(perm)
        assert read.code == "resume.read"


class TestRoleSchemas:
    def test_create_valid(self) -> None:
        role = RoleCreate(organization_id=_uuid(), name="editor")
        assert role.name == "editor"

    def test_read_from_attributes(self) -> None:
        role = Role(
            id=_uuid(),
            organization_id=_uuid(),
            name="admin",
            description=None,
            is_system=False,
        )
        read = RoleRead.model_validate(role)
        assert read.name == "admin"
        assert read.is_system is False


class TestMembershipSchemas:
    def test_read_from_attributes(self) -> None:
        m = Membership(
            id=_uuid(),
            user_id=_uuid(),
            organization_id=_uuid(),
            role_id=_uuid(),
            is_active=True,
            joined_at=_now(),
        )
        read = MembershipRead.model_validate(m)
        assert read.is_active is True


class TestAuditLogSchemas:
    def test_read_from_attributes(self) -> None:
        log = AuditLog(
            id=_uuid(),
            action="user.deleted",
            target_type="user",
            created_at=_now(),
        )
        read = AuditLogRead.model_validate(log)
        assert read.action == "user.deleted"
        assert read.target_type == "user"
