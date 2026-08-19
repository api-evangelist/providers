---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The public WordPress REST API behind antaresrx.com. This is the content management surface for the corporate marketing site and its press-release / in-the-media newsroom -- it is NOT a first-party pro
  name: Antares Therapeutics WordPress REST API
  slug: antares-therapeutics-wordpress-rest
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/antares-therapeutics-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antares-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antaresrx.com
- group: company
  title: ''
  type: Blog
  url: https://antaresrx.com/category/press-release/
- group: company
  title: ''
  type: BlogRSS
  url: https://antaresrx.com/feed/
- group: company
  title: ''
  type: News
  url: https://antaresrx.com/category/in-the-media/
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/antaresrx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antaresrx.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antaresrx.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antares-therapeutics/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/antares_rx
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/antares_rx
- group: agent
  title: ''
  type: WellKnown
  url: well-known/antares-therapeutics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/antares-therapeutics-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/antares-therapeutics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/antares-therapeutics-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/antares-therapeutics-vulnerability-disclosure.yml
created: '2026-07-17'
description: Antares Therapeutics is a Boston- and South San Francisco-based precision medicine company developing small-molecule therapies against validated but previously undruggable targets in cancer and other serious diseases. Spun out of Scorpion Therapeutics following Eli Lilly's March 2025 acquisition of Scorpion, Antares launched in June 2025 with a $177 million Series A co-led by Omega Funds, Atlas Venture, Lightspeed Venture Partners, BVF Partners and Cormorant Asset Management. The company combines medicinal chemistry (proprietary compound libraries and next-generation mass spectrometry to find new chemical pockets), target biology (first-in-class preclinically validated targets and allosteric approaches to clinically validated ones), and predictive sciences (physics-based modeling, machine learning and molecular dynamics) to shorten discovery cycles. Its most advanced program is expected to enter the clinic in 2026, with multiple additional preclinical programs and discovery
  collaborations with Novartis, AstraZeneca and Pierre Fabre Laboratories. Antares is a private, preclinical-stage biotechnology company and publishes no public product API, developer portal or SDK surface.
image: https://antaresrx.com/wp-content/uploads/2025/06/logo-antaresrx-2x.png
layout: provider
mcp_servers:
- description: ''
  name: antares-therapeutics-mcp.yml
  slug: antares-therapeutics-mcpyml
modified: '2026-07-19'
name: Antares Therapeutics
nav: Providers
network: true
overview: 'Antares Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Precision Medicine, and Oncology.


  Antares Therapeutics'' developer surface includes engineering blog, product news, authentication, and 14 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.7
  delta: -1.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/antares-therapeutics/refs/heads/main/screenshots/antares-therapeutics-2026-07-25T200338.png
security:
- kind: authentication
  name: Antares Therapeutics Authentication
  slug: antares-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Antares Therapeutics Domain Security
  slug: antares-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Antares Therapeutics Vulnerability Disclosure
  slug: antares-therapeutics-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: antares-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Precision Medicine
- Oncology
- Drug Discovery
- Life Sciences
- Machine Learning
website: https://antaresrx.com
---
