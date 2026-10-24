from pydantic import BaseModel, Field


class EnrichedCompanyLead(BaseModel):
    domain: str
    company_name: str
    industry: str
    estimated_employees: str
    tech_stack: list[str] = Field(default_factory=list)
    decision_makers: list[dict[str, str]] = Field(default_factory=list)
    contact_email: str | None = None
    headquarters: str | None = None
    social_profiles: dict[str, str] = Field(default_factory=dict)
    fit_score: int = Field(ge=1, le=10, description="1 is poor fit, 10 is ideal customer profile")
