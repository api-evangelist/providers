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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/openevidence-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openevidence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openevidence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openevidence.com/
- group: start
  title: ''
  type: Signup
  url: https://www.openevidence.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.openevidence.com/signin
- group: other
  title: ''
  type: Announcements
  url: https://www.openevidence.com/announcements
- group: company
  title: ''
  type: About
  url: https://www.openevidence.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.openevidence.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.openevidence.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.openevidence.com/announcements
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openevidence
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openevidence
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/openevidence
- group: company
  title: ''
  type: Partnerships
  url: ''
- group: company
  title: ''
  type: Investors
  url: ''
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: other
  title: ''
  type: BusinessModel
  url: ''
- group: other
  title: ''
  type: Adoption
  url: ''
created: '2026-05-23'
description: OpenEvidence is a clinical decision-support search platform that uses generative AI grounded in peer-reviewed medical literature to answer clinical questions for verified clinicians. The product is free for U.S. licensed clinicians and is monetized through pharmaceutical advertising; partnerships include the New England Journal of Medicine, JAMA, NCCN, and the Cochrane Library. As of 2026 it serves more than 860,000 verified clinicians. OpenEvidence does not currently expose a public self-service developer API.
features:
- description: AI-powered medical search that returns answers grounded in peer-reviewed medical literature with inline citations.
  name: Evidence-Grounded Search
- description: Hands-free voice interface allowing clinicians to ask clinical questions and receive spoken, evidence-based answers across web and mobile.
  name: Voice Mode
- description: Real-time clinical intelligence delivered during the patient visit.
  name: Visits
- description: Generative-AI feature that supports medical coding workflows.
  name: AI Medical Coding
- description: Account access restricted to verified U.S. licensed healthcare professionals.
  name: Clinician Verification
- description: Available as web and mobile applications, free for verified clinicians.
  name: Mobile and Web
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openevidence.png
layout: provider
modified: '2026-05-23'
name: OpenEvidence
nav: Providers
network: true
overview: 'OpenEvidence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Clinical Decision Support, Medical AI, Generative AI, and Evidence-Based Medicine.


  OpenEvidence''s developer surface includes signup flow, engineering blog, authentication, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openevidence/refs/heads/main/screenshots/openevidence-2026-06-20T190957.png
security:
- kind: domain-security
  name: Openevidence Domain Security
  slug: openevidence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Openevidence Vulnerability Disclosure
  slug: openevidence-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Openevidence Trust Center
  slug: openevidence-trust-center
  summary_line: SOC 2, HIPAA
slug: openevidence
tags:
- Healthcare
- Clinical Decision Support
- Medical AI
- Generative AI
- Evidence-Based Medicine
- Search
- Voice
use_cases:
- description: Clinicians query OpenEvidence at the point of care for diagnostic, therapeutic, and management questions.
  name: Point-of-Care Decision Support
- description: Use by medical residents and trainees for evidence lookup.
  name: Medical Education
- description: AI medical coding workflows for revenue-cycle support.
  name: Coding and Documentation
website: https://www.openevidence.com/
---
