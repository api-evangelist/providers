---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Advanceai Agentic Access
  operation_count: 9
  slug: advanceai-agentic-access
  summary_line: 9 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.advance.ai
  baseurl_source: declared
  description: eKYC building blocks — token authentication, Global Document Verification (SDK licensing, OCR field extraction, ID forgery detection), face comparison, and liveness detection with video evidence and P
  name: ADVANCE.AI Open API
  slug: advanceai-open-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/advanceai-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://advance.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.advance.ai/global_document_verification.html
- group: docs
  title: ''
  type: APIReference
  url: https://doc.advance.ai/liveness_detection.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.advance.ai/
- group: operate
  title: ''
  type: Support
  url: https://support.advance.ai/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://advance.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advance.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advance.ai/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://advance.ai/book-free-demo/
- group: auth
  title: ''
  type: Compliance
  url: https://advance.ai/security-compliance/
- group: auth
  title: ''
  type: Security
  url: security/advanceai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/advanceai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advanceai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/advanceai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advanceai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/advanceai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/advanceai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/advanceai-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advanceai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/advanceai-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advanceai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advanceai-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/advanceai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/advanceai-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/advanceai-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/advanceai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advanceai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/advanceai-open-api-overlay.yaml
created: '2026-09-07'
description: 'ADVANCE.AI is the digital identity verification, KYC/KYB, AML, compliance and risk-management business unit of Advance Intelligence Group, headquartered in Singapore and founded in 2016. Its AdvanGuard product line covers identity verification, document verification, face authentication and Know Your Business checks for banking and financial services, fintech, crypto, payments, e-commerce and the sharing economy, with a strong footprint across Southeast Asia and other emerging markets. ADVANCE.AI publishes a public Open API at api.advance.ai documented at doc.advance.ai — token authentication, Global Document Verification with OCR field extraction and ID forgery detection, face comparison, and liveness detection with video evidence and PII data retention — plus first-party Android and iOS capture SDKs distributed from its own Maven and object-storage endpoints. Onboarding is sales-led: there is no self-service sign-up and no published pricing, and platform access keys are issued
  through the Websaas platform.'
image: https://advance.ai/wp-content/uploads/2025/09/top-header-right-image.webp
layout: provider
modified: '2026-09-07'
name: ADVANCE.AI
nav: Providers
network: true
overview: 'ADVANCE.AI publishes 1 API on the [APIs.io](https://apis.io/) network: Open API. Tagged areas include Company, Identity Verification, KYC, KYB, and AML.


  ADVANCE.AI''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Advanceai Plans Pricing
  plan_count: 0
  slug: advanceai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Advanceai Rate Limits
  slug: advanceai-rate-limits
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.8
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Advanceai Authentication
  slug: advanceai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Advanceai Domain Security
  slug: advanceai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Advanceai Vulnerability Disclosure
  slug: advanceai-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Advanceai Trust Center
  slug: advanceai-trust-center
  summary_line: trust center published
slug: advanceai
tags:
- Company
- Identity Verification
- KYC
- KYB
- AML
- Fraud Prevention
- Face Recognition
- Liveness Detection
- OCR
- Document Verification
- Risk Management
- Artificial Intelligence
- Fintech
- Singapore
website: https://advance.ai/
---
