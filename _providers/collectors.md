---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Collectors Agentic Access
  operation_count: 6
  slug: collectors-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.psacard.com/publicapi
  baseurl_source: declared
  description: The PSA Public API Methods API from Collectors — 6 operation(s) for psa public api methods.
  name: Collectors PSA Public API Methods API
  slug: collectors-psa-public-api-methods-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PSA Public PSA Public API Methods API
  slug: open-collectors-psa-public-api-methods-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.collectors.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.psacard.com/publicapi/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api.psacard.com/publicapi/swagger
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.psacard.com/publicapi
- group: start
  title: ''
  type: SignUp
  url: https://www.psacard.com/publicapi
- group: company
  title: ''
  type: Blog
  url: https://blog.collectors.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.collectors.com/collectorsuseragreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.collectors.com/privacypolicy
- group: auth
  title: ''
  type: Authentication
  url: authentication/collectors-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/collectors-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/collectors-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/collectors-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/collectors-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/collectors-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/collectors-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/collectors-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/collectors-psa-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/collectors-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/collectors-domain-security.yml
created: '2026-07-17'
description: Collectors (Collectors Holdings, Inc.) is the parent company behind PSA, PCGS, Beckett, SGC, Card Ladder, and Collectors vault and financial services — the infrastructure powering trust, authentication, grading, vaulting, and marketplace services for trading cards, coins, currency, and memorabilia. Its PSA brand publishes a public developer API for certificate verification, grading order and submission tracking, and population reports, secured with Bearer access tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/collectors.png
layout: provider
modified: '2026-07-18'
name: Collectors
nav: Providers
network: true
overview: 'Collectors publishes 1 API on the [APIs.io](https://apis.io/) network: PSA Public API Methods API. Tagged areas include Company, Marketplace, Collectibles, Authentication, and Grading.


  Collectors'' developer surface includes documentation, API reference, signup flow, engineering blog, authentication, and 15 more developer resources.'
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/collectors/refs/heads/main/screenshots/collectors-2026-07-25T210048.png
security:
- kind: authentication
  name: Collectors Authentication
  slug: collectors-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Collectors Domain Security
  slug: collectors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: collectors
tags:
- Company
- Marketplace
- Collectibles
- Authentication
- Grading
- Trading Cards
- Verification
website: https://www.collectors.com
---
