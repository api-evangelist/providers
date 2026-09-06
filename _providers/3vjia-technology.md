---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://open-gateway.3vjia.com
  baseurl_source: declared
  description: 'The 3vjia (三维家) Open Platform API — 429 documented POST operations on open-gateway.3vjia.com covering account and single-sign-on management, design schemes, product and material libraries, quotation, '
  name: 3vjia Open Platform API
  slug: 3vjia-technology-open-platform-api
artifact_total: 9
asyncapis:
- description: ''
  name: 3Vjia Technology Webhooks
  slug: 3vjia-technology-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.3vjia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.3vjia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.3vjia.com/v1/document
- group: docs
  title: ''
  type: APIReference
  url: https://dev.3vjia.com/v1/document
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.3vjia.com/v1/document?apiId=d39aed16895f4f4bb88df99d38f93fb3
- group: start
  title: ''
  type: SignUp
  url: https://dev.3vjia.com/manage/my-app/developer
- group: start
  title: ''
  type: Login
  url: https://admin.3vjia.com/
- group: operate
  title: ''
  type: Support
  url: https://www.3vjia.com/helpcenter
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.3vjia.com/helpcenter
- group: company
  title: ''
  type: Blog
  url: https://www.3vjia.com/tag
- group: commercial
  title: ''
  type: Pricing
  url: https://mall.3vjia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3vj-fcontent.3vjia.com/agreement/2e6ef94b22b34d9db98e4ac9c28965eb.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/3vjia-technology-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/3vjia-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/3vjia-technology-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/3vjia-technology-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/3vjia-technology-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/3vjia-technology-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3vjia-technology-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3vjia-technology-llms.txt
- group: design
  title: ''
  type: Components
  url: components/3vjia-technology-components.yml
created: '2026-09-05'
description: 3vjia Technology (Guangdong Sanweijia Information Technology Co., Ltd. / 三维家, international brand AiHouse) is a Guangzhou-based home-furnishing industrial-software company founded in 2013 that runs a cloud 3D design and manufacturing platform for the interior-decoration and custom-furniture industry. Its products span 3D cloud design, AI Dream Home (AI梦想家), AI Light Design (AI轻设计), CAD and rendering engines, the DMS order-splitting system, the MOS/MCS manufacturing execution systems and the AIMES manufacturing platform, joining design, quotation, order placement, splitting and factory production into one chain. It operates a public Open Platform (dev.3vjia.com) whose gateway open-gateway.3vjia.com exposes 429 documented POST operations covering accounts and SSO, design schemes, product/material libraries, quotation, orders, production batches, floor plans and generative AI, authenticated with OAuth 2.0 client credentials issued against graph.3vjia.com.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-09-05'
name: 3vjia Technology
nav: Providers
network: true
overview: '3vjia Technology publishes 1 API on the [APIs.io](https://apis.io/) network: 3vjia Open Platform API. Tagged areas include Company, 3D Design, Home Furnishing, Interior Design, and Manufacturing.


  The 3vjia Technology catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  3vjia Technology''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: 3Vjia Technology Plans Pricing
  plan_count: 4
  slug: 3vjia-technology-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: 3Vjia Technology Rate Limits
  slug: 3vjia-technology-rate-limits
scopes:
- name: 3Vjia Technology Scopes
  scope_count: 0
  slug: 3vjia-technology-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 60.4
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 3Vjia Technology Authentication
  slug: 3vjia-technology-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: 3Vjia Technology Domain Security
  slug: 3vjia-technology-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: 3Vjia Technology Vulnerability Disclosure
  slug: 3vjia-technology-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: 3Vjia Technology Trust Center
  slug: 3vjia-technology-trust-center
  summary_line: trust center published
slug: 3vjia-technology
tags:
- Company
- 3D Design
- Home Furnishing
- Interior Design
- Manufacturing
- Custom Furniture
- CAD
- Rendering
- Artificial Intelligence
- SaaS
- China
- Open Platform
website: https://www.3vjia.com/
---
