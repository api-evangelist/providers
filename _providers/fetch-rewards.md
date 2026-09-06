---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Receipts API from Fetch Rewards — 2 operation(s) for receipts.
  name: Fetch Rewards Receipts API
  slug: fetch-rewards-receipts-api
artifact_total: 4
collections:
- collection_type: open
  name: Receipt Processor
  slug: open-fetch-rewards-receipt-processor
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fetch-rewards-receipt-processor-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://fetch.com/
- group: company
  title: ''
  type: Blog
  url: https://fetch.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.fetch.com/hc/en-us
- group: operate
  title: ''
  type: FAQ
  url: https://fetch.com/faq
- group: operate
  title: ''
  type: ContactUs
  url: https://business.fetch.com/contact-us
- group: company
  title: ''
  type: Newsroom
  url: https://business.fetch.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://fetch.com/careers/jobs
- group: build
  title: ''
  type: Extensions
  url: https://chromewebstore.google.com/detail/fetch/hgpkkikfhmllgfnclpfiklpcpehelhda
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fetch-rewards
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fetch.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fetch.com/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fetch-rewards-llc/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/FetchRewards
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/fetchrewards_vdp
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fetch-rewards-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fetch-rewards-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fetch-rewards-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fetch-rewards-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/fetch-rewards-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fetch-rewards-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fetch-rewards-llms.txt
created: '2026-08-01'
description: Fetch (legally Fetch Rewards, LLC) is a Madison, Wisconsin consumer rewards platform whose mobile app lets shoppers scan paper receipts, connect e-receipts and link accounts to earn points redeemable for gift cards and other rewards. On the demand side, Fetch For Business sells consumer packaged goods brands, retailers and restaurants receipt-verified offers, video and display advertising, point boosts, loyalty programs and omnichannel audience activation, all measured against real purchase data and managed through its Mission Control campaign platform. Fetch publishes no public developer or partner API and operates no developer portal; its only public machine-readable contract is the Receipt Processor reference OpenAPI it publishes on GitHub as an engineering hiring exercise. It does run a coordinated vulnerability disclosure program via HackerOne and publishes an RFC 9116 security.txt, and its GitHub organization ships several first-party open-source Swift and Python developer
  libraries.
image: https://fetch.com/favicon.png
layout: provider
modified: '2026-08-01'
name: Fetch Rewards
nav: Providers
network: true
overview: 'Fetch Rewards publishes 1 API on the [APIs.io](https://apis.io/) network: Receipts API. Tagged areas include Company, Rewards, Loyalty, Consumer, and Retail.


  Fetch Rewards'' developer surface includes engineering blog, support, FAQ, and 19 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 42.9
    developer_ergonomics: 7.1
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 25.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fetch-rewards/refs/heads/main/screenshots/fetch-rewards-2026-08-07T165248.png
security:
- kind: domain-security
  name: Fetch Rewards Domain Security
  slug: fetch-rewards-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fetch Rewards Vulnerability Disclosure
  slug: fetch-rewards-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: fetch-rewards
tags:
- Company
- Rewards
- Loyalty
- Consumer
- Retail
- Advertising
- Receipts
- Consumer Packaged Goods
- Mobile
- Marketing
website: https://fetch.com/
---
