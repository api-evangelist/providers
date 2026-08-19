---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prudential-plc-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prudential-plc-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prudential-plc-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prudential-plc-hk-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prudential-plc-sg-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prudential-plc-id-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prudential-plc-vn-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prudential-plc-ph-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prudential-plc-my-prubsn-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/prudential-plc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prudential-plc-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/prudential-plc-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.prudentialplc.com/en/
- group: company
  title: ''
  type: About
  url: https://www.prudentialplc.com/en/about-us/our-purpose-and-mission/
- group: other
  title: ''
  type: Technology
  url: https://www.prudentialplc.com/en/about-us/our-strategy/technology/
- group: other
  title: ''
  type: Distribution
  url: https://www.prudentialplc.com/en/about-us/our-strategy/distribution/
- group: company
  title: ''
  type: Blog
  url: https://www.prudentialplc.com/en/newsroom/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.prudentialplc.com/en/investors/overview/
- group: operate
  title: ''
  type: Contact
  url: https://www.prudentialplc.com/en/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prudentialplc.com/en/site-services/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prudentialplc.com/en/site-services/terms-of-use/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PrudentialCorporationAsia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prudentialplc
- group: other
  title: ''
  type: ResponsibleAI
  url: https://www.prudentialplc.com/en/site-services/responsible-ai-at-prudential/
- group: other
  title: ''
  type: Policies
  url: https://www.prudentialplc.com/en/about-us/corporate-governance-and-corporate-actions/policies-and-statements/
- group: company
  title: ''
  type: Careers
  url: https://www.prudentialplc.com/en/careers/overview/
- group: other
  title: ''
  type: Sitemap
  url: https://www.prudentialplc.com/sitemap.xml
- group: company
  title: ''
  type: Website
  url: https://www.prudential.com.hk/
- group: company
  title: ''
  type: Website
  url: https://www.prudential.com.sg/
- group: company
  title: ''
  type: Website
  url: https://www.prudential.co.id/
- group: company
  title: ''
  type: Website
  url: https://www.prudential.com.vn/
- group: company
  title: ''
  type: Website
  url: https://www.prulifeuk.com.ph/
- group: company
  title: ''
  type: Website
  url: https://www.prubsn.com.my/
created: '2026-07-25'
description: 'Prudential plc is a life and health insurance and asset management group incorporated in England and Wales and listed on the London, Hong Kong, Singapore and New York exchanges, with its principal operating office in Hong Kong and roots in London going back to 1848. Its home market for this profile is the United Kingdom, but its book is almost entirely Asian and African: life protection, health and medical, savings and retirement, takaful, pensions and Hong Kong Mandatory Provident Funds, plus asset management under the Eastspring brand, across Hong Kong, Singapore, Malaysia, Indonesia, the Philippines, Thailand, Vietnam, Taiwan, India, mainland China, Cambodia, Laos, Myanmar and a dozen African markets including Kenya, Uganda, Ghana, Nigeria and Zambia. It is no longer a UK retail insurer at all - the UK and Europe business was demerged as M&G plc in 2019 and the US business as Jackson Financial in 2021 - so the familiar UK "Pru" brands at pru.co.uk belong to M&G, not to this
  company. Its API posture is that there is no public API posture. Prudential plc publishes no developer portal, no API reference, no downloadable OpenAPI or Swagger document and no partner integration surface of any kind: developer, developers, docs, api, apis, partners, portal and sandbox subdomains of prudentialplc.com all fail to resolve, and /developers, /api, /developer, /partners and /integrations on the corporate site all return HTTP 404. The group''s stated technology strategy is inward-facing - AI, automation, cloud and a global AI Lab running over a hundred internal use cases - and its distribution is built on tied agency forces and exclusive bancassurance partnerships with banks such as Standard Chartered, CIMB, MSB, SeABank, Bank Syariah Indonesia and UOB, which are commercial and contractual relationships rather than published API programmes. The Pulse by Prudential health and wealth app onboards health-tech and wealth-tech partners (Babylon, Tictrac, Halodoc, Smarter Health,
  Prive Technologies, OVO, Google Cloud) but every announcement describes the arrangement in commercial terms and none exposes a developer programme, SDK or public API. No ACORD, AL3, ACORD XML or NGDS reference was found anywhere in Prudential plc''s public estate. Recorded honestly as a large carrier with a fully partner-gated, non-public integration surface. One genuine machine-readable surface does exist, and it is not an API: six of the group''s market operating companies - Prudential Hong Kong, Prudential Singapore, Prudential Indonesia, Prudential Vietnam, Pru Life UK in the Philippines and Prudential BSN Takaful in Malaysia - publish real first-party llms.txt documents for grounding large language models, with Prudential Vietnam declaring a per-user-agent bot access policy for gptbot, claudebot, google-extended, perplexitybot and six other crawlers. The corporate domain publishes none. Underneath that, the group runs a visibly centralised security posture: TLS 1.3 and HSTS on every
  market host, and one shared PowerDMARC/PowerSPF tenant with a common aggregate-report mailbox across all seven domains, at p=reject on the corporate domain and p=quarantine in the markets, with no CAA record anywhere.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Prudential plc
nav: Providers
network: true
overview: 'Prudential plc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Life Insurance, Health Insurance, and Carrier.


  Prudential plc''s developer surface includes engineering blog and 32 more developer resources.'
random_paper: 103
score:
  band: emerging
  composite: 15.9
  delta: -0.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 16.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Prudential Plc Domain Security
  slug: prudential-plc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prudential-plc
tags:
- Insurance
- United Kingdom
- Life Insurance
- Health Insurance
- Carrier
- Asset Management
- Pensions
- Takaful
- Bancassurance
- Asia
- Africa
- Hong Kong
- Singapore
- Malaysia
- Indonesia
- Vietnam
- Philippines
- Eastspring
- Responsible AI
- llms.txt
website: https://www.prudentialplc.com/en/
---
