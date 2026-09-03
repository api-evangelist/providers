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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-financial-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: The only host recorded for this profile, www.american-financial.com, is a parked domain listed for sale — it CNAMEs to traff-https.hugedomains.com and redirects to hugedomains.com/domain_profile.cfm?d=american-financial.com — so there is no company site, developer portal, or API surface behind this name at all; the Fortune 500 company of a similar name is American Financial Group, profiled separately as american-financial-group.
  evidence:
  - status: 200
    url: https://www.american-financial.com
  - status: 200
    url: https://www.hugedomains.com/domain_profile.cfm?d=american-financial.com
  - status: 404
    url: https://www.american-financial.com/.well-known/agent-card.json
  - status: 302
    url: https://www.american-financial.com/openapi.json
  reason: defunct
  state: none
created: '2024-11-15'
description: 'American Financial is a financial-services profile in the API Evangelist catalog for which no operating company could be resolved on 2026-09-02. The only host ever recorded for it, american-financial.com, is not run by a business: it is a CNAME to traff-https.hugedomains.com and redirects to a HugeDomains "this domain is for sale" listing, so there is no website, no developer program, no documentation and no machine-readable API artifact behind this name. The Fortune 500 insurance and annuities holding company American Financial Group, Inc. (NYSE: AFG, Great American Insurance Group) is a different company and is profiled separately in this catalog as american-financial-group, where its Great American Carrier Services APIs belong.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-financial.png
layout: provider
modified: '2026-09-02'
name: American Financial
nav: Providers
network: true
overview: American Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services and Finance.
random_paper: 4
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 93.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-financial/refs/heads/main/screenshots/american-financial-2026-06-20T171914.png
security:
- kind: domain-security
  name: American Financial Domain Security
  slug: american-financial-domain-security
  summary_line: TLSv1.3
slug: american-financial
tags:
- Financial-Services
- Finance
---
