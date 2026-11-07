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
  band: agent-aware
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Documentation page describing Mimo's API concepts and usage.
  name: Mimo API
  slug: mimo-api
- description: 'Mimo API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Mimo API
  slug: mimo-org-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/mimo-org/rules/mimo-org-rules.yml
  title: ''
  type: Spectral
  url: rules/mimo-org-rules.yml
- group: design
  href: https://artifacts.apis.io/mimo-org/json-ld/mimo-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mimo-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/mimo-org/vocabulary/mimo-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mimo-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mimo-org/data-model/mimo-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mimo-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/mimo-org/conformance/mimo-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mimo-org-conformance.yml
- group: other
  href: https://artifacts.apis.io/mimo-org/hosts/mimo-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mimo-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/mimo-org/vendors/mimo-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mimo-org-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://mimo.org/glossary/programming-concepts/webhook
- group: operate
  title: ''
  type: Support
  url: https://support.mimo.org/hc/en-us
- group: start
  title: ''
  type: Sandbox
  url: https://mimo.org/glossary/python/console
- group: docs
  title: ''
  type: Documentation
  url: https://mimo.org/glossary/programming-concepts/documentation
- group: auth
  href: https://artifacts.apis.io/mimo-org/security/mimo-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mimo-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mimo.org/
- group: company
  title: ''
  type: Blog
  url: https://mimo.org/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mimo.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mimo.org/privacy
- group: start
  title: ''
  type: SignUp
  url: https://mimo.org/web/login
coverage:
  checked: '2026-10-29'
  detail: Mimo provides a coding education platform but does not publish a developer program or public API.
  evidence:
  - status: 200
    url: https://mimo.org/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Mimo is an interactive coding education platform that teaches programming languages such as Python, JavaScript, HTML, and CSS through gamified lessons. Founded in 2014 in Vienna, Austria, it offers mobile and web apps for learners to build real‑world skills at their own pace. Backed by Techstars, Mimo serves millions of users worldwide.
image: https://support.mimo.org/hc/theming_assets/01HZM5S83BW0QAQ6X8RRY8V5F5
json_schemas:
- name: PostWebhooksPaymentRequest
  property_count: 5
  slug: mimo-org-post-webhooks-payment-request
- name: PostWebhooksPaymentResponse
  property_count: 1
  slug: mimo-org-post-webhooks-payment-response
jsonld:
- class_count: 2
  name: Mimo Org Context
  property_count: 6
  slug: mimo-org-context
layout: provider
modified: '2026-10-29'
name: Mimo
nav: Providers
network: true
overview: 'Mimo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Coding, Mobile App, and Learning Platform.


  The Mimo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mimo''s developer surface includes support, sandbox, documentation, engineering blog, signup flow, and 12 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Mimo API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mimo-org-rules
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 3.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mimo-org/mimo-org-2026-11-03T135615.png
security:
- kind: domain-security
  name: Mimo Org Domain Security
  slug: mimo-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mimo-org
tags:
- Company
- Education
- Coding
- Mobile App
- Learning Platform
website: https://mimo.org/
---
