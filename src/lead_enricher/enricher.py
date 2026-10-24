from lead_enricher.models import EnrichedCompanyLead

DATABASE = {
    "stripe.com": EnrichedCompanyLead(
        domain="stripe.com",
        company_name="Stripe, Inc.",
        industry="Fintech / Payment Processing",
        estimated_employees="5,000 - 10,000",
        tech_stack=["Ruby", "Python", "React", "AWS", "Kafka"],
        decision_makers=[
            {"name": "Patrick Collison", "role": "CEO"},
            {"name": "David Singleton", "role": "CTO"},
        ],
        contact_email="press@stripe.com",
        headquarters="San Francisco, CA / Dublin, Ireland",
        social_profiles={"linkedin": "https://linkedin.com/company/stripe", "twitter": "https://x.com/stripe"},
        fit_score=9,
    ),
    "shopify.com": EnrichedCompanyLead(
        domain="shopify.com",
        company_name="Shopify Inc.",
        industry="E-Commerce Platforms",
        estimated_employees="10,000+",
        tech_stack=["Ruby on Rails", "GraphQL", "React", "Google Cloud"],
        decision_makers=[
            {"name": "Tobi Lutke", "role": "CEO"},
            {"name": "Harley Finkelstein", "role": "President"},
        ],
        contact_email="contact@shopify.com",
        headquarters="Ottawa, Canada",
        social_profiles={"linkedin": "https://linkedin.com/company/shopify", "twitter": "https://x.com/shopify"},
        fit_score=10,
    ),
    "notion.so": EnrichedCompanyLead(
        domain="notion.so",
        company_name="Notion Labs, Inc.",
        industry="Productivity & Collaboration Software",
        estimated_employees="500 - 1,000",
        tech_stack=["TypeScript", "React", "Next.js", "PostgreSQL", "AWS"],
        decision_makers=[
            {"name": "Ivan Zhao", "role": "CEO"},
            {"name": "Akshay Kothari", "role": "COO"},
        ],
        contact_email="team@makenotion.com",
        headquarters="San Francisco, CA",
        social_profiles={"linkedin": "https://linkedin.com/company/notionhq", "twitter": "https://x.com/notionhq"},
        fit_score=8,
    ),
}


def enrich_domain(domain: str) -> EnrichedCompanyLead:
    clean_domain = domain.lower().replace("https://", "").replace("http://", "").split("/")[0].strip()

    if clean_domain in DATABASE:
        return DATABASE[clean_domain]

    name = clean_domain.split(".")[0].capitalize()
    return EnrichedCompanyLead(
        domain=clean_domain,
        company_name=name,
        industry="Technology / General",
        estimated_employees="10 - 50",
        tech_stack=["Python", "Cloud Infrastructure"],
        decision_makers=[{"name": "Founder", "role": "Managing Director"}],
        contact_email=f"contact@{clean_domain}",
        headquarters="Global / Remote",
        social_profiles={"linkedin": f"https://linkedin.com/company/{name.lower()}"},
        fit_score=5,
    )
