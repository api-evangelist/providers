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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://brainly.com
- group: commercial
  title: ''
  type: Pricing
  url: https://brainly.com/app/brainlyplus
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.brainly.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brainly.com/pages/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainly.com/pages/privacy_policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brainly
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/brainly-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brainly-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brainly-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brainly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://brainly.com/responsible-disclosure-program
created: '2026-07-17'
description: Brainly is an education technology company founded in 2009 in Krakow, Poland (originally Zadane.pl) and now headquartered in New York City. It operates the world's largest online learning and homework-help community, a gamified, crowdsourced social-learning network where students, parents, and teachers ask and answer academic questions with verified answers from peers, educators, and Brainly's proprietary AI. As of 2025 the platform serves over 350 million monthly users across roughly 35 countries and has evolved from a community Q&A product into an agentic AI Learning Companion spanning homework help, AI tutoring, test prep, and classroom participation. Brainly is a consumer subscription business (Brainly Plus); it publishes no official public developer API — this profile captures its public web, security, and policy surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brainly.png
layout: provider
modified: '2026-07-18'
name: Brainly
nav: Providers
network: true
overview: 'Brainly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Education, EdTech, and Learning.


  Brainly''s developer surface includes pricing and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 14.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Brainly Domain Security
  slug: brainly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brainly Vulnerability Disclosure
  slug: brainly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brainly
tags:
- Company
- Consumer
- Education
- EdTech
- Learning
- Homework Help
- AI Tutor
- Community
website: https://brainly.com
---
