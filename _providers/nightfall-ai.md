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
    error_semantics: documented
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
  score: 22.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nightfall Ai Agentic Access
  operation_count: 1
  slug: nightfall-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Scan API from Nightfall AI — 1 operation(s) for scan.
  name: Nightfall AI Scan API
  slug: nightfall-ai-scan-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nightfall AI Scan API
  slug: open-nightfall-ai-scan-api
- collection_type: open
  name: Nightfall AI Scan Scans API
  slug: open-nightfall-ai-scans-api
- collection_type: open
  name: Nightfall AI
  slug: open-nightfall-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nightfall-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nightfall-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nightfall-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nightfall-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nightfall-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nightfallai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nightfall-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://help.nightfall.ai/firewall-for-ai/introduction/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://help.nightfall.ai/firewall-for-ai/introduction/pricing
- group: design
  title: ''
  type: ErrorCodes
  url: https://help.nightfall.ai/firewall-for-ai/key-concepts/errors
- group: operate
  title: ''
  type: FAQ
  url: https://help.nightfall.ai/firewall-for-ai/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nightfall.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nightfall.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.nightfall.ai/blog
- group: docs
  title: ''
  type: Guide
  url: https://www.nightfall.ai/guides
- group: company
  title: ''
  type: Partners
  url: https://www.nightfall.ai/partners
- group: start
  title: ''
  type: Login
  url: https://auth.nightfall.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://help.nightfall.ai/firewall-for-ai/introduction/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://help.nightfall.ai/firewall-for-ai/introduction/pricing
- group: design
  title: ''
  type: ErrorCodes
  url: https://help.nightfall.ai/firewall-for-ai/key-concepts/errors
- group: operate
  title: ''
  type: FAQ
  url: https://help.nightfall.ai/firewall-for-ai/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nightfall.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nightfall.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.nightfall.ai/blog
- group: docs
  title: ''
  type: Guide
  url: https://www.nightfall.ai/guides
- group: company
  title: ''
  type: Partners
  url: https://www.nightfall.ai/partners
created: '2024-07-02T00:00:00.000Z'
description: Nightfall AI is a data security platform that specializes in identifying and protecting sensitive information within an organization. By utilizing machine learning technology, Nightfall AI can automatically scan files, emails, and messages to detect and classify sensitive data such as credit card numbers, social security numbers, and personal addresses.
finops:
- name: Nightfall Ai Finops
  service_category: API
  slug: nightfall-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nightfall-ai.png
layout: provider
modified: '2026-05-19'
name: Nightfall AI
nav: Providers
network: true
overview: 'Nightfall AI publishes 1 API on the [APIs.io](https://apis.io/) network: Scan API. Tagged areas include Artificial Intelligence, Privacy, and Sensitive Data.


  Nightfall AI''s developer surface includes authentication, getting-started guide, pricing, FAQ, engineering blog, and 21 more developer resources.'
plans:
- name: Nightfall Ai Plans Pricing
  plan_count: 3
  slug: nightfall-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Nightfall Ai Rate Limits
  slug: nightfall-ai-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nightfall-ai/refs/heads/main/screenshots/nightfall-ai-2026-06-20T190326.png
security:
- kind: authentication
  name: Nightfall Ai Authentication
  slug: nightfall-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nightfall Ai Domain Security
  slug: nightfall-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nightfall Ai Vulnerability Disclosure
  slug: nightfall-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Nightfall Ai Trust Center
  slug: nightfall-ai-trust-center
  summary_line: SOC 2, HIPAA
slug: nightfall-ai
tags:
- Artificial Intelligence
- Privacy
- Sensitive Data
---
