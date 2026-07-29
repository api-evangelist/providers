---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: jAccount is SJTU's identity and single sign-on system. It provides OAuth 2.0 and OpenID Connect authorization for third-party member sites, including an authorization endpoint, token endpoint, and use
  name: jAccount Single Sign-On (OAuth 2.0 / OIDC)
  slug: jaccount-oauth
- description: A GraphQL-based data resources API providing access to institutional data categories including account information, faculty/staff data, undergraduate teaching records, and academic papers. Queries are
  name: SJTU Data Resources GraphQL API
  slug: data-graphql
- description: GraphQL APIs exposing undergraduate teaching and course-related information. Course interfaces return current academic year data. Part of the gated data resources platform.
  name: Undergraduate Teaching APIs
  slug: graphql-student
- description: GraphQL APIs providing faculty and staff profile data. Part of the gated data resources platform requiring an approved application.
  name: Faculty APIs
  slug: graphql-faculty
- description: GraphQL APIs providing access to academic paper and publication metadata. Part of the gated data resources platform requiring an approved application.
  name: Academic Paper APIs
  slug: graphql-paper
- description: GraphQL APIs used to retrieve account-related information. Access requires an approved data resource application.
  name: Account APIs
  slug: graphql-account
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shanghai-jiao-tong-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.sjtu.edu.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sjtu.edu.cn/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.sjtu.edu.cn/auth/oidc.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sjtug
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/shanghai-jiao-tong-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/shanghai-jiao-tong-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shanghai-jiao-tong-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shanghai-jiao-tong-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Shanghai Jiao Tong University (SJTU), founded in 1896 and located in Shanghai, China (Mainland), is one of China''s top research universities and is ranked #56 in the QS World University Rankings 2025. SJTU operates an official developer platform (developer.sjtu.edu.cn) that exposes internal data resources and infrastructure to authorized developers. Its public-facing programmable footprint centers on the jAccount single sign-on system (OAuth 2.0 / OpenID Connect) and a GraphQL-based data resources platform covering account, faculty, undergraduate teaching, and academic paper data. Access to the data APIs is gated behind an application and approval process; the SSO/OIDC integration is documented publicly.'
finops:
- name: Shanghai Jiao Tong University Finops
  service_category: Education
  slug: shanghai-jiao-tong-university-finops
graphqls:
- description: A GraphQL-based data resources API providing access to institutional data categories including account information, faculty/staff data, undergraduate teaching records, and academic papers. Queries are
  name: Shanghai Jiao Tong University GraphQL API
  slug: shanghai-jiao-tong-university-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shanghai-jiao-tong-university.png
jsonld:
- class_count: 7
  name: Shanghai Jiao Tong University Context
  property_count: 4
  slug: shanghai-jiao-tong-university-context
layout: provider
modified: '2026-06-03'
name: Shanghai Jiao Tong University
nav: Providers
network: true
overview: 'Shanghai Jiao Tong University publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The Shanghai Jiao Tong University catalog on APIs.io includes 1 JSON-LD context.


  Shanghai Jiao Tong University''s developer surface includes authentication, GitHub presence, and 8 more developer resources.'
plans:
- name: Shanghai Jiao Tong University Plans Pricing
  plan_count: 2
  slug: shanghai-jiao-tong-university-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 1
  name: Shanghai Jiao Tong University Rate Limits
  slug: shanghai-jiao-tong-university-rate-limits
score:
  band: emerging
  composite: 22.8
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shanghai-jiao-tong-university/refs/heads/main/screenshots/shanghai-jiao-tong-university-2026-06-20T193853.png
security:
- kind: domain-security
  name: Shanghai Jiao Tong University Domain Security
  slug: shanghai-jiao-tong-university-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: shanghai-jiao-tong-university
tags:
- Education
- Higher Education
- University
- Research
- China
- GraphQL
- Identity
- OpenID Connect
website: https://en.sjtu.edu.cn/
---
