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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Pangea Agentic Access
  operation_count: 18
  slug: pangea-agentic-access
  summary_line: 18 operations · 18 acting
api_count: 1
apis:
- description: Detect and redact malicious content in LLM inputs and outputs.
  name: Pangea AI Guard API
  slug: pangea-ai-guard-api
- description: Hosted authentication, user lifecycle, and session management.
  name: Pangea AuthN API
  slug: pangea-authn-api
- description: Domain and URL reputation lookups.
  name: Pangea Domain Intel API
  slug: pangea-domain-intel-api
- description: Scan files for malicious content.
  name: Pangea File Scan API
  slug: pangea-file-scan-api
- description: IP reputation, geolocation, and VPN/proxy enrichment.
  name: Pangea IP Intel API
  slug: pangea-ip-intel-api
- description: Detect and remove sensitive information from text and structured data.
  name: Pangea Redact API
  slug: pangea-redact-api
- description: Tamper-proof, cryptographically verifiable audit logging.
  name: Pangea Secure Audit Log API
  slug: pangea-secure-audit-log-api
- description: Secrets and cryptographic key management.
  name: Pangea Vault API
  slug: pangea-vault-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pangea Security Services AI Guard API
  slug: open-pangea-ai-guard-api
- collection_type: open
  name: Pangea Security Services AI Guard AuthN API
  slug: open-pangea-authn-api
- collection_type: open
  name: Pangea Security Services AI Guard Domain Intel API
  slug: open-pangea-domain-intel-api
- collection_type: open
  name: Pangea Security Services AI Guard File Scan API
  slug: open-pangea-file-scan-api
- collection_type: open
  name: Pangea Security Services AI Guard IP Intel API
  slug: open-pangea-ip-intel-api
- collection_type: open
  name: Pangea Security Services AI Guard Redact API
  slug: open-pangea-redact-api
- collection_type: open
  name: Pangea Security Services AI Guard Secure Audit Log API
  slug: open-pangea-secure-audit-log-api
- collection_type: open
  name: Pangea Security Services AI Guard Vault API
  slug: open-pangea-vault-api
- collection_type: open
  name: Pangea Security Services API
  slug: open-pangea
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pangea-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pangea-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pangea-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pangea-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://pangea.cloud/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pangeacyber
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pangeacyber
- group: company
  title: ''
  type: Website
  url: https://pangea.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://pangea.cloud/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/pangea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pangea-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pangea-finops.yml
created: '2026-06-20'
description: Pangea delivers security as a set of composable, API-first services - authentication (AuthN/AuthZ), tamper-proof Secure Audit Log, Redact, Vault, File Scan, URL/Domain/IP Intel, Embargo, Sanitize, and AI Guard / Prompt Guard - that developers call over REST with a Bearer service token to add security guardrails to applications and AI workloads.
finops:
- name: Pangea Finops
  service_category: Security
  slug: pangea-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pangea.png
layout: provider
modified: '2026-06-20'
name: Pangea
nav: Providers
network: true
overview: 'Pangea publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AI Guard API, AuthN API, Domain Intel API, and 5 more. Tagged areas include Security, AI Security, Authentication, Audit Log, and Data Protection.


  Pangea''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Pangea Plans Pricing
  plan_count: 3
  slug: pangea-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Pangea Rate Limits
  slug: pangea-rate-limits
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pangea/refs/heads/main/screenshots/pangea-2026-06-20T191339.png
security:
- kind: authentication
  name: Pangea Authentication
  slug: pangea-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pangea Domain Security
  slug: pangea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pangea Trust Center
  slug: pangea-trust-center
  summary_line: SOC 2, ISO 27001
slug: pangea
tags:
- Security
- AI Security
- Authentication
- Audit Log
- Data Protection
website: https://pangea.cloud/
---
