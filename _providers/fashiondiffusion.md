---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'REST API for asynchronous AI fashion generation tasks. Authenticates with a single long-lived bearer API key (Authorization: Bearer fd_live_xxx); the secret is shown only once at creation and a key ma'
  name: Fashion Diffusion Public API
  slug: fashion-diffusion-public-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fashiondiffusion-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fashiondiffusion.ai/playground/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fashiondiffusion.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.fashiondiffusion.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fashiondiffusion.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fashiondiffusion.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.fashiondiffusion.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FashionDiffusion
- group: operate
  title: ''
  type: Support
  url: mailto:support@fashiondiffusion.ai
- group: design
  title: ''
  type: Conformance
  url: conformance/fashiondiffusion-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/fashiondiffusion-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fashiondiffusion-llms.txt
created: '2026-08-31'
description: 'AI fashion design and commercial photography platform for brands and creators, offering a generative AI fashion suite — virtual try-on, AI model and outfit generation, flat lay production, background change and removal, garment recolor, face swap and fashion video. Fashion Diffusion exposes a bearer-key REST Public API at https://www.fashiondiffusion.ai/api/public/v1/ built on a submit-and-poll task model: a generation request returns HTTP 202 with a task id, and the caller polls until the task reaches SUCCEEDED or FAILED. The published reference documents four operations across two capabilities — Virtual Try-On and AI Inpainting submission plus task query and cursor-paginated task list — while marketing advertises more than 18 endpoints. There is no OpenAPI, GraphQL schema, Postman collection, MCP server, agent card, SDK, webhook surface, status page or changelog, and the reference states plainly that this version carries no idempotency protection.'
image: https://zhiyi-image.oss-cn-hangzhou.aliyuncs.com/devops/comfyui/input/demo/web-assets/fd-web/v20260806/images/product-hero/home.webp
layout: provider
modified: '2026-08-31'
name: Fashion Diffusion
nav: Providers
network: true
overview: 'Fashion Diffusion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fashion, E-Commerce, Retail, Generative AI, and Image-Generation.


  Fashion Diffusion''s developer surface includes pricing, signup flow, engineering blog, support, and 8 more developer resources.'
plans:
- name: Fashiondiffusion Plans Pricing
  plan_count: 4
  slug: fashiondiffusion-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Fashiondiffusion Rate Limits
  slug: fashiondiffusion-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 35.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Fashiondiffusion Authentication
  slug: fashiondiffusion-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fashiondiffusion Domain Security
  slug: fashiondiffusion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fashiondiffusion
tags:
- Fashion
- E-Commerce
- Retail
- Generative AI
- Image-Generation
- Virtual Try-On
- Computer-Vision
- Video Generation
- Product Photography
- Creative / Design Tools
website: https://www.fashiondiffusion.ai/playground/api
---
