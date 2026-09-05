---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://developers.sendinblue.com/docs'', ''status'': 301, ''note'': ''declared website redirects to https://developers.brevo.com/docs — a different registrable domain (sendinblue.com -> brevo.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://developers.sendinblue.com/docs
  baseurl_source: declared
  description: A service that provides solutions relating to marketing and/or transactional email and/or SMS
  name: Sendinblue
  slug: sendinblue
artifact_total: 4
asyncapis:
- description: AsyncAPI description of the outbound webhook surface for Brevo (formerly Sendinblue). Brevo delivers event notifications by issuing HTTP POST requests with a JSON body to a URL configured by the custo
  name: Brevo (Sendinblue) Webhooks
  slug: sendinblue-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendinblue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.sendinblue.com/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: A service that provides solutions relating to marketing and/or transactional email and/or SMS
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendinblue.png
layout: provider
modified: '2026-05-30'
name: Sendinblue
nav: Providers
network: true
overview: 'Sendinblue publishes 1 API on the [APIs.io](https://apis.io/) network: Sendinblue. Tagged areas include Email and Public APIs.


  The Sendinblue catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 15
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Sendinblue API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: sendinblue-asyncapi-spectral-rules
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.8
    catalog_earned_first_party: 0.0
    catalog_gap: 84.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 11.4
    contract_quality: 45.8
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 11.4
    operational_transparency: 0.0
  previous_composite: 18.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendinblue/refs/heads/main/screenshots/sendinblue-2026-06-20T193701.png
security:
- kind: domain-security
  name: Sendinblue Domain Security
  slug: sendinblue-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sendinblue
tags:
- Email
- Public APIs
website: https://developers.sendinblue.com/docs
---
