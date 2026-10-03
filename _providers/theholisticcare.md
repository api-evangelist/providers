---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Theholisticcare Agentic Access
  operation_count: 3
  slug: theholisticcare-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: A free, public, read‑only REST API exposing structured mindfulness resources such as research citations, glossary, games, audio practices, and blog excerpts.
  name: THC Open Mindfulness Resources API
  slug: thc-open-mindfulness-resources-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Health API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for health.
  name: The Holistic Care — THC Open Mindfulness API Health API
  slug: theholisticcare-health-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Resources API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for resources.
  name: The Holistic Care — THC Open Mindfulness API Resources API
  slug: theholisticcare-resources-api
- baseURL: https://api.theholisticcare.com
  baseurl_source: spec
  description: The Search API from The Holistic Care — THC Open Mindfulness API — 1 operation(s) for search.
  name: The Holistic Care — THC Open Mindfulness API Search API
  slug: theholisticcare-search-api
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/theholisticcare/refs/heads/main/security/theholisticcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theholisticcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.theholisticcare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.theholisticcare.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.theholisticcare.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.theholisticcare.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.theholisticcare.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theholisticcare.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.theholisticcare.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.theholisticcare.com/login
created: '2026-09-28'
description: The THC Open Mindfulness Resources API, provided by The Holistic Care, offers a free, public, read‑only REST API delivering structured mindfulness resources. It includes research citations, a glossary, 16 mindfulness games, 111 guided audio practices, and excerpts from 527 blog posts. The API requires no authentication, API key, or cost, and supports searching and browsing across all resource families via the /v1/resources and /v1/search endpoints.
layout: provider
modified: '2026-09-28'
name: The Holistic Care — THC Open Mindfulness API
nav: Providers
network: true
overview: 'The Holistic Care — THC Open Mindfulness API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Health API, Resources API, Search API, and 1 more. Tagged areas include Mindfulness, Education, Health, OpenAPI, and Public APIs.


  The The Holistic Care — THC Open Mindfulness API catalog on APIs.io includes 1 Spectral governance ruleset.


  The Holistic Care — THC Open Mindfulness API''s developer surface includes documentation, engineering blog, support, signup flow, and 5 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 1
  name: Theholisticcare Rate Limits
  slug: theholisticcare-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: The Holistic Care — THC Open Mindfulness API API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: theholisticcare-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.5
    catalog_earned_first_party: 8.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 39.8
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Theholisticcare Domain Security
  slug: theholisticcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: theholisticcare
tags:
- Mindfulness
- Education
- Health
- OpenAPI
- Public APIs
- Free
website: https://api.theholisticcare.com/
---
