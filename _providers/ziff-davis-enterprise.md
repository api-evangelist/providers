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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ziff-davis-enterprise-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ziff-davis-enterprise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/ziff-davis-enterprise-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ziff-davis-enterprise-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ziff-davis-enterprise-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ziff-davis-enterprise-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ziff-davis-enterprise-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ziffdavis.com
- group: company
  title: ''
  type: Blog
  url: https://www.ziffdavis.com/about/news
- group: operate
  title: ''
  type: Support
  url: https://www.ziffdavis.com/about/contacts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ziffdavis.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ziffdavis.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ziffdavis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ziff-davis-inc
coverage:
  checked: '2026-08-13'
  detail: Ziff Davis, Inc. is the publicly traded parent of a portfolio of consumer and B2B media brands and ships no API of its own — the corporate WordPress site returns 404 for /openapi.json, /graphql, /mcp, /llms.txt and every /.well-known/ path, and its only machine surface, the WordPress REST root at /wp-json/, answers 401 to anonymous callers.
  evidence:
  - status: 404
    url: https://www.ziffdavis.com/openapi.json
  - status: 404
    url: https://www.ziffdavis.com/graphql
  - status: 404
    url: https://www.ziffdavis.com/.well-known/api-catalog
  - status: 404
    url: https://www.ziffdavis.com/llms.txt
  - status: 401
    url: https://www.ziffdavis.com/wp-json/
  - status: 200
    url: https://www.ziffdavis.com/page-sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Ziff Davis (Nasdaq: ZD) is a vertically focused digital media and internet company whose portfolio includes leading brands across technology, entertainment, shopping, health, cybersecurity, and marketing technology. Its brands include PCMag, Mashable, IGN, Lifehacker, RetailMeNot, Spiceworks, Everyday Health, IPVanish, Ookla (Speedtest), FullContact, and iContact, among others. The company operates a portfolio of advertising, subscription, and performance-marketing businesses rather than a single first-party public API product. This API Evangelist profile was surfaced as an Insight Partners portfolio lead; a public web crawl of the corporate site found an active investor-relations, newsroom, brands, privacy, and terms surface but no developer portal, API reference, or published API specification at the corporate (ziffdavis.com) level. A second enrichment pass on 2026-08-13 ran full contract discovery against www.ziffdavis.com — OpenAPI, Swagger, GraphQL, MCP, llms.txt and every
  /.well-known/ path returned 404, and the WordPress REST root returned 401 — confirming the absence, while surfacing three real corporate programs: a Bugcrowd-hosted Responsible Vulnerability Disclosure Program, a published data-protection compliance program (Data Privacy Framework self-certification for 32 named group entities, GDPR DPAs, CCPA request metrics, EU DSA statement, NIST SP 800-88 vendor security exhibit), and five first-party PHP packages in the ziffdavis Packagist namespace — none of which is an API client library. Ziff Davis brands with their own API surfaces are profiled as separate entries.'
image: https://www.ziffdavis.com/wp-content/uploads/2021/09/Ziff-Davis_Blue.png
layout: provider
modified: '2026-08-13'
name: Ziff Davis Enterprise
nav: Providers
network: true
overview: 'Ziff Davis Enterprise is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Media, Internet, Publishing, and Cybersecurity.


  Ziff Davis Enterprise''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Ziff Davis Enterprise Plans Pricing
  plan_count: 0
  slug: ziff-davis-enterprise-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 0
  name: Ziff Davis Enterprise Rate Limits
  slug: ziff-davis-enterprise-rate-limits
score:
  band: emerging
  composite: 16.8
  delta: 0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 16.4
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Ziff Davis Enterprise Domain Security
  slug: ziff-davis-enterprise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ziff Davis Enterprise Vulnerability Disclosure
  slug: ziff-davis-enterprise-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: ziff-davis-enterprise
tags:
- Company
- Digital Media
- Internet
- Publishing
- Cybersecurity
- Marketing Technology
- Technology
- Publicly Traded
website: https://www.ziffdavis.com
---
