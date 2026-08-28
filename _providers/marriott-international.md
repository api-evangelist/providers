---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Marriott International Agentic Access
  operation_count: 5
  slug: marriott-international-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 3
apis:
- description: Check room availability and rates.
  name: Marriott International Availability API
  slug: marriott-international-availability-api
- description: Search and retrieve hotel property information.
  name: Marriott International Properties API
  slug: marriott-international-properties-api
- description: Create and manage hotel reservations.
  name: Marriott International Reservations API
  slug: marriott-international-reservations-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Marriott Developer Availability API
  slug: open-marriott-international-availability-api
- collection_type: open
  name: Marriott Developer API
  slug: open-marriott-international-developer-api
- collection_type: open
  name: Marriott Developer Availability Properties API
  slug: open-marriott-international-properties-api
- collection_type: open
  name: Marriott Developer Availability Reservations API
  slug: open-marriott-international-reservations-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marriott-international-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/marriott-international-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marriott-international-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marriott-international-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/marriott-international-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marriott-international
description: Marriott International is a global lodging company with a portfolio of more than 30 brands and thousands of properties across luxury, premium, select, and longer-stay hotel categories.
finops:
- name: Marriott International Finops
  service_category: Hospitality Distribution API
  slug: marriott-international-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marriott-international.png
layout: provider
modified: '2026-05-19'
name: Marriott International
nav: Providers
network: true
overview: 'Marriott International publishes 3 APIs on the [APIs.io](https://apis.io/) network: Availability API, Properties API, and Reservations API. Tagged areas include Fortune 500.


  Marriott International''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Marriott International Plans Pricing
  plan_count: 1
  slug: marriott-international-plans-pricing
press:
- date: '2026-05-25'
  title: Marriott CIO talks enterprisewide AI deployment strategy
  url: https://www.hoteldive.com/news/marriott-cio-talks-enterprisewide-ai-deployment-strategy/820467/
- date: '2026-05-25'
  title: Marriott gears up for another year of major tech spending
  url: https://www.ciodive.com/news/marriott-international-tech-spend-digital-transformation-plan-ai/715036/
- date: '2026-05-25'
  title: '📌 A lesson from Marriott International''s bold #AI strategy.'
  url: https://www.linkedin.com/posts/michaelcohen-growth-advisor-travel-and-hospitality-tech_ai-aiforhospitality-gainadvisors-activity-7371929050979868672-oz0w
- date: '2026-05-25'
  title: Press Release - Marriott International Media Centre
  url: https://marriott.pressarea.com/pressrelease
- date: '2026-05-25'
  title: How Marriott's AI Initiatives Will Empower Event Planners
  url: https://marriottbonvoyevents.com/news-and-highlights/article/674/how-marriott-s-ai-initiatives-will-empower-event-planners
random_paper: 17
rate_limits:
- limit_count: 2
  name: Marriott International Rate Limits
  slug: marriott-international-rate-limits
scopes:
- name: Marriott International Scopes
  scope_count: 2
  slug: marriott-international-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: emerging
  composite: 25.0
  delta: 1.9
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marriott-international/refs/heads/main/screenshots/marriott-international-2026-06-20T185001.png
security:
- kind: authentication
  name: Marriott International Authentication
  slug: marriott-international-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Marriott International Domain Security
  slug: marriott-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Marriott International Vulnerability Disclosure
  slug: marriott-international-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: marriott-international
tags:
- Fortune 500
---
