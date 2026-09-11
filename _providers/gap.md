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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gap-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gapinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gap-inc-
- group: company
  title: ''
  type: Website
  url: https://www.gap.com
- group: other
  title: ''
  type: Corporate
  url: https://www.gapinc.com/
- group: build
  title: ''
  type: Packages
  url: packages/gap-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gap-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gap-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/gap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gap.com/customer-service/terms-of-use?cid=6754
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gapinc.com/en-us/consumer-privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.gap.com/customer-service/contact-us?cid=81270
- group: company
  title: ''
  type: Blog
  url: https://www.gapinc.com/en-us/news/technology
coverage:
  checked: '2026-09-10'
  detail: Gap Inc. provisioned an Apigee developer portal at developer.gap.com — the DNS still CNAMEs to gap-api-docs-portal.apigee.net — but the service behind it is gone, its TLS certificate covers only *.apigee.net, and the Apigee runtime at api.gap.com answers every anonymous path with "Unable to identify proxy for host", so there is no public API, spec, portal or SDK to read anywhere on the estate.
  evidence:
  - status: 0
    url: https://developer.gap.com/
  - status: 404
    url: https://gap-api-docs-portal.apigee.net/
  - status: 404
    url: https://api.gap.com/openapi.json
  - status: 404
    url: https://www.gap.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'Gap Inc. is a Fortune 500 American clothing and accessories retailer operating the Gap, Old Navy, Banana Republic and Athleta brands. Gap Inc. publishes no public developer API, no machine-readable contract and no developer portal: probing found an Apigee gateway at api.gap.com that exposes no proxy to an anonymous caller, and a dangling developer-portal CNAME at developer.gap.com (gap-api-docs-portal.apigee.net) whose service is gone and whose TLS certificate does not cover the hostname. What Gap does publish is a HackerOne vulnerability disclosure programme and one first-party open-source Android HTTP library. This repository is an independent third-party profile of that public surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gap.png
layout: provider
modified: '2026-09-10'
name: Gap
nav: Providers
network: true
overview: 'Gap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Retail, Apparel, E-Commerce, and Fashion.


  Gap''s developer surface includes support, engineering blog, and 12 more developer resources.'
press:
- date: '2026-05-25'
  title: Gap Inc. Taps Gemini Enterprise to Become 'AI-First' Retailer
  url: https://www.chiefmarketer.com/gap-inc-taps-gemini-enterprise-to-become-ai-first-retailer/
- date: '2026-05-25'
  title: Gap goes all-in on Google AI. Old Navy, Banana Republic ...
  url: https://www.facebook.com/groups/augmented/posts/1338047877377594/
- date: '2026-05-25'
  title: Gap Inc. Sets Out to Reimagine Retail Powered by Google ...
  url: https://www.prnewswire.com/news-releases/gap-inc-sets-out-to-reimagine-retail-powered-by-google-clouds-ai-302579074.html
- date: '2026-05-25'
  title: Gap Inc. Is Using AI to Reimagine Retail, With New ...
  url: https://www.gapinc.com/en-us/articles/2025/11/gap-inc-is-using-ai-to-reimagine-retail,-with-new-
- date: '2026-05-25'
  title: Inspectorio's AI Platform Will Enable Greater Traceability in ...
  url: https://www.businesswire.com/news/home/20260409206762/en/Inspectorios-AI-Platform-Will-Enable-Greater-Traceability-in-Gap-Inc.-Global-Supply-Chain
random_paper: 18
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 4.4
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gap Domain Security
  slug: gap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gap Vulnerability Disclosure
  slug: gap-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: gap
tags:
- Fortune 500
- Retail
- Apparel
- E-Commerce
- Fashion
- Consumer Goods
website: https://www.gap.com
---
