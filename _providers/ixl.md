---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ixl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ixl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ixl.com
- group: other
  title: ''
  type: ForFamilies
  url: https://www.ixl.com/membership/family
- group: other
  title: ''
  type: ForTeachers
  url: https://www.ixl.com/membership/teachers
- group: other
  title: ''
  type: ForSchools
  url: https://www.ixl.com/membership/schools
- group: other
  title: ''
  type: ForAdministrators
  url: https://www.ixl.com/membership/administrators
- group: build
  title: ''
  type: TechIntegration
  url: https://www.ixl.com/membership/administrators/tech-integration
- group: other
  title: ''
  type: Diagnostic
  url: https://www.ixl.com/inspiration/diagnostic
- group: agent
  title: ''
  type: SkillPlans
  url: https://www.ixl.com/standards
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ixl.com/membership/family/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.ixl.com/help-center
- group: other
  title: ''
  type: ClassLinkRostering
  url: https://www.ixl.com/materials/us/integration/Auto-rostering_with_ClassLink_on_IXL.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ixl.com/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ixl.com/termsofservice
- group: company
  title: ''
  type: AboutUs
  url: https://www.ixl.com/company
- group: company
  title: ''
  type: Careers
  url: https://www.ixl.com/company/careers
- group: company
  title: ''
  type: Blog
  url: https://blog.ixl.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ixl-learning
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ixllearning
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/IXLlearning
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/ixllearning
- group: operate
  title: ''
  type: Support
  url: https://www.ixl.com/help-center/contact
created: '2026-05-23'
description: 'IXL Learning is a K-12 personalized practice platform with 17,000+ skills across Math, Language Arts, Science, Social Studies, and Spanish, plus the IXL Real-Time Diagnostic and skill recommendations. IXL is sold primarily as a SaaS subscription to families, teachers, schools, and districts. Its integration surface is school-rostering and SSO, not a public developer API: IXL supports Clever (SSO + rostering), ClassLink (SSO + OneRoster auto-rostering), OneRoster CSV/REST, LTI, Google Classroom, and SAML SSO for district deployments. There is no public REST API portal, no published OpenAPI, and no partner developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ixl.png
layout: provider
modified: '2026-05-23'
name: IXL Learning
nav: Providers
network: true
overview: 'IXL Learning is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, K-12, Math, Language Arts, and Science.


  IXL Learning''s developer surface includes pricing, engineering blog, YouTube channel, support, and 19 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.2
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ixl/refs/heads/main/screenshots/ixl-2026-06-20T183642.png
security:
- kind: domain-security
  name: Ixl Domain Security
  slug: ixl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ixl Vulnerability Disclosure
  slug: ixl-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ixl
tags:
- Education
- K-12
- Math
- Language Arts
- Science
- Social Studies
- Spanish
- Diagnostic
- Rostering
- SSO
website: https://www.ixl.com
---
