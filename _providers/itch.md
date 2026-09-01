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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.itchpet.com
created: '2026-07-17'
description: Itch is a UK direct-to-consumer pet wellness brand, backed by Seedcamp, offering a subscription service that delivers vet-approved flea, tick and worm treatments to pet owners on a recurring schedule, alongside pet health guidance and related care products. It was surfaced as a Seedcamp portfolio company and added to the API Evangelist network for enrichment. As of this pass no public developer portal, API documentation, or machine-readable API specification could be found; the consumer website sits behind bot protection, so this profile carries provider identity plus a probed domain-security posture rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/itch.png
layout: provider
modified: '2026-07-19'
name: Itch
nav: Providers
network: true
overview: Itch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pets, Pet Care, Pet Wellness, and Subscription.
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/itch/refs/heads/main/screenshots/itch-2026-07-25T222959.png
security:
- kind: domain-security
  name: Itch Domain Security
  slug: itch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: itch
tags:
- Company
- Pets
- Pet Care
- Pet Wellness
- Subscription
- Consumer
- E-Commerce
website: https://www.itchpet.com
---
