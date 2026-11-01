---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Full endpoint reference for the Poggio REST API.
  name: Poggio API
  slug: poggio-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/poggiolabs-com/plans/poggiolabs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/poggiolabs-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/poggiolabs-com/llms/poggiolabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/poggiolabs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/poggiolabs-com/hosts/poggiolabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/poggiolabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/poggiolabs-com/vendors/poggiolabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/poggiolabs-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poggio.io/docs/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poggio.io/docs/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/poggiolabs-com/security/poggiolabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/poggiolabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poggio.io
- group: docs
  title: ''
  type: Documentation
  url: https://poggio.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://poggio.io/pricing
coverage:
  checked: '2026-10-25'
  detail: Documentation is served as a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://poggio.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Poggio Labs provides AI‑powered revenue agents that research accounts, build strategic plans, and execute revenue operations at scale for enterprise sales teams. Their platform integrates with Salesforce and Slack to deliver real‑time intelligence, automated account planning, and next‑action recommendations, helping sellers close deals faster.
image: https://poggio.io/api/og?type=site&title=Account+plans+that+write+themselves%2C+in+Slack+and+Salesforce&description=Poggio+puts+actionable+intelligence+at+the+center+of+your+revenue+org%2C+guiding+sellers+and+agents+with+tailored+POVs+%28Points+of+View%29%2C+automated+account+plans%2C+and+next+actions+that+move+deals+forward.&s=d2614426316313f2
layout: provider
modified: '2026-10-25'
name: Poggio Labs
nav: Providers
network: true
overview: 'Poggio Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Sales, Revenue, Enterprise, and Automation.


  Poggio Labs'' developer surface includes documentation, pricing, and 8 more developer resources.'
plans:
- name: Poggiolabs Com Plans Pricing
  plan_count: 3
  slug: poggiolabs-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Poggiolabs Com Domain Security
  slug: poggiolabs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: poggiolabs-com
tags:
- AI
- Sales
- Revenue
- Enterprise
- Automation
- Company
website: https://poggio.io
---
