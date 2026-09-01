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
  url: security/knote-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://knote.com
created: '2026-07-17'
description: 'Knote is a small New York-based startup backed by 500 Global, surfaced through the 500 Global portfolio and added to the API Evangelist network as an enrichment lead. Third-party company databases describe it inconsistently: Tracxn profiles Knote as a knowledge-management platform that raised roughly $150K from 500 Global, while Dealroom describes it as an AI-powered email summarization and management tool. No first-party description could be confirmed. As of the 2026-07-19 enrichment pass the knote.com web property is offline — the domain resolves (Cloudflare nameservers, an EC2 A record, live Google Workspace MX and an SPF record including Mailgun and Mailchimp) but refuses connections on both port 80 and port 443, so no homepage, developer portal, documentation, API reference, or machine-readable specification could be retrieved. No corporate GitHub organization, package-registry client library, or public API surface was found; the GitHub repositories named "Knote" are unrelated
  third-party note-taking and Kubernetes-course projects. This profile therefore carries only what could be independently verified: the funding and identity facts above plus a live DNS/TLS domain-security probe. It should be treated as a dormant or defunct lead and re-checked if the domain returns to service.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knote.png
layout: provider
modified: '2026-07-19'
name: Knote
nav: Providers
network: true
overview: Knote is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Startup, Knowledge-Management, Notes, and Productivity.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
security:
- kind: domain-security
  name: Knote Domain Security
  slug: knote-domain-security
  summary_line: no transport/DNS hardening detected
slug: knote
tags:
- Company
- Startup
- Knowledge-Management
- Notes
- Productivity
- Collaboration
- 500 Global
- Dormant
website: https://knote.com
---
