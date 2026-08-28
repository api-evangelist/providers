---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Adsense Agentic Access
  operation_count: 5
  slug: google-adsense-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: The Accounts API from Google AdSense Management — 1 operation(s) for accounts.
  name: Google AdSense Management Accounts API
  slug: google-adsense-accounts-api
- description: The Adclients API from Google AdSense Management — 1 operation(s) for adclients.
  name: Google AdSense Management Adclients API
  slug: google-adsense-adclients-api
- description: The Adunits API from Google AdSense Management — 1 operation(s) for adunits.
  name: Google AdSense Management Adunits API
  slug: google-adsense-adunits-api
- description: The Payments API from Google AdSense Management — 1 operation(s) for payments.
  name: Google AdSense Management Payments API
  slug: google-adsense-payments-api
- description: The Reports:generate API from Google AdSense Management — 1 operation(s) for reports:generate.
  name: Google AdSense Management Reports:generate API
  slug: google-adsense-reports-generate-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google AdSense Management Accounts API
  slug: open-google-adsense-accounts-api
- collection_type: open
  name: Google AdSense Management Accounts Adclients API
  slug: open-google-adsense-adclients-api
- collection_type: open
  name: Google AdSense Management Accounts Adunits API
  slug: open-google-adsense-adunits-api
- collection_type: open
  name: Google AdSense Management Accounts Payments API
  slug: open-google-adsense-payments-api
- collection_type: open
  name: Google AdSense Management Accounts Reports:generate API
  slug: open-google-adsense-reports-generate-api
- collection_type: open
  name: Google AdSense Management API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-adsense-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-adsense-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-adsense-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-adsense-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-adsense-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-adsense
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/adsense/management/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://support.google.com/adsense/answer/180195
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google AdSense Management API allows publishers to access their inventory and run earnings and performance reports. Publishers can manage ad clients, ad units, custom channels, URL channels, and access payment and policy information programmatically.
finops:
- name: Google Adsense Finops
  service_category: API
  slug: google-adsense-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-adsense.png
layout: provider
modified: '2026-05-19'
name: Google AdSense Management
nav: Providers
network: true
overview: 'Google AdSense Management publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Adclients API, Adunits API, and 2 more. Tagged areas include Ad Units, AdSense, Advertising, Monetization, and Publishers.


  The Google AdSense Management catalog on APIs.io includes 1 Spectral governance ruleset.


  Google AdSense Management''s developer surface includes authentication, getting-started guide, pricing, and 7 more developer resources.'
plans:
- name: Google Adsense Plans Pricing
  plan_count: 3
  slug: google-adsense-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Google Adsense Rate Limits
  slug: google-adsense-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google AdSense Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-adsense-jsonschema-spectral-rules
scopes:
- name: Google Adsense Scopes
  scope_count: 2
  slug: google-adsense-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 32.5
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-adsense/refs/heads/main/screenshots/google-adsense-2026-06-20T182008.png
security:
- kind: authentication
  name: Google Adsense Authentication
  slug: google-adsense-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Adsense Domain Security
  slug: google-adsense-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Adsense Vulnerability Disclosure
  slug: google-adsense-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-adsense
tags:
- Ad Units
- AdSense
- Advertising
- Monetization
- Publishers
- Reports
- Revenue
---
