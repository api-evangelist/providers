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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The USTC Open Source Software Mirror, operated by the campus Linux User Group (LUG @ USTC), is one of the largest open source software mirror services among universities in mainland China, hosting Deb
  name: USTC Open Source Software Mirror
  slug: mirrors
- description: passport.ustc.edu.cn is the university's unified single sign-on / identity authentication service used by most campus websites and systems. It is a gated authentication endpoint for members of the ins
  name: USTC Unified Identity Authentication (Passport SSO)
  slug: passport
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ustc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.ustc.edu.cn/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ustclug
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-science-and-technology-of-china/
- group: operate
  title: ''
  type: Status
  url: https://mirrors.ustc.edu.cn/status/
- group: auth
  title: ''
  type: Authentication
  url: https://passport.ustc.edu.cn/
- group: commercial
  title: ''
  type: Plans
  url: plans/ustc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ustc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ustc-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ustc-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The University of Science and Technology of China (USTC, 中国科学技术大学) is a public research university in Hefei, Anhui, China, founded in 1958 under the Chinese Academy of Sciences. It is ranked #63 in the QS World University Rankings 2025. USTC does not publish a centralized, public developer portal or documented institutional API program. Its most visible publicly reachable technical footprint is the USTC Open Source Software Mirror operated by the campus Linux User Group (LUG @ USTC), along with a unified SSO/identity service and a campus GitLab. Most academic, library, and SIS systems sit behind the passport.ustc.edu.cn single sign-on and are not openly documented.'
finops:
- name: Ustc Finops
  service_category: Education
  slug: ustc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ustc.png
jsonld:
- class_count: 13
  name: Ustc Context
  property_count: 2
  slug: ustc-context
layout: provider
modified: '2026-06-03'
name: University of Science and Technology of China
nav: Providers
network: true
overview: 'University of Science and Technology of China publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and China.


  The University of Science and Technology of China catalog on APIs.io includes 1 JSON-LD context.


  University of Science and Technology of China''s developer surface includes GitHub presence, status page, authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Ustc Plans Pricing
  plan_count: 2
  slug: ustc-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Ustc Rate Limits
  slug: ustc-rate-limits
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ustc/refs/heads/main/screenshots/ustc-2026-06-20T200827.png
security:
- kind: domain-security
  name: Ustc Domain Security
  slug: ustc-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ustc
tags:
- Education
- Higher Education
- University
- Research
- China
- Open Source Mirror
website: https://en.ustc.edu.cn/
---
