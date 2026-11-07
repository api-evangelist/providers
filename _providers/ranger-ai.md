---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.rangerx.ai/security
- group: agent
  href: https://artifacts.apis.io/ranger-ai/llms/ranger-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ranger-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/ranger-ai/hosts/ranger-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ranger-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/ranger-ai/vendors/ranger-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ranger-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rangerx.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://www.rangerx.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rangerx.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.rangerx.ai/blog
- group: auth
  href: https://artifacts.apis.io/ranger-ai/security/ranger-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ranger-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ranger-ai/security/ranger-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ranger-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ranger-ai/security/ranger-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ranger-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rangerx.ai
coverage:
  checked: '2026-10-22'
  detail: Homepage loads a JavaScript‑rendered single‑page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.rangerx.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Ranger AI, operating as Ranger RFX Inc., provides an AI‑powered intelligence layer for industrial engineering. It helps organizations automate RFP responses, evaluate tenders, and review contracts by extracting answers from technical documents and citing sources. The platform targets procurement automation, engineering document analysis, and enterprise AI applications, delivering accurate, citation‑backed insights to streamline decision‑making in industrial contexts.
image: https://www.rangerx.ai/opengraph-image?06853850e504d81d
layout: provider
modified: '2026-10-21'
name: Ranger AI
nav: Providers
network: true
overview: 'Ranger AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Industrial Engineering, Procurement, and Document Automation.


  Ranger AI''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ranger-ai/ranger-ai-2026-11-03T141924.png
security:
- kind: domain-security
  name: Ranger Ai Domain Security
  slug: ranger-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Ranger Ai Vulnerability Disclosure
  slug: ranger-ai-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Ranger Ai Trust Center
  slug: ranger-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: ranger-ai
tags:
- Company
- Artificial Intelligence
- Industrial Engineering
- Procurement
- Document Automation
website: https://rangerx.ai
---
