---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-12'
api_count: 13
apis:
- description: Operations for managing account-level resources
  name: 10Web Account API
  slug: 10web-account-api
- description: Operations for backup management
  name: 10Web Backup API
  slug: 10web-backup-api
- description: Operations for website builder and page management
  name: 10Web Builder API
  slug: 10web-builder-api
- description: Operations for cache management
  name: 10Web Cache API
  slug: 10web-cache-api
- description: Operations for SSL certificate management
  name: 10Web Certificate API
  slug: 10web-certificate-api
- description: Operations for domain management
  name: 10Web Domain API
  slug: 10web-domain-api
- description: Operations for PHP version management
  name: 10Web PHP Management API
  slug: 10web-php-management-api
- description: Operations for AI-powered features
  name: 10Web Section Based AI API
  slug: 10web-section-based-ai-api
- description: Operations for subdomain management
  name: 10Web Subdomain API
  slug: 10web-subdomain-api
- description: Operations for WordPress Vibe Coding - AI-powered website content generation
  name: 10Web Vibe Coding API
  slug: 10web-vibe-coding-api
- description: Operations for website creation and management
  name: 10Web Website API
  slug: 10web-website-api
- description: Operations for secure WordPress admin panel autologin functionality
  name: 10Web WP Autologin API
  slug: 10web-wp-autologin-api
- description: Operations for DNS zone management
  name: 10Web Zone API
  slug: 10web-zone-api
artifact_total: 17
asyncapis:
- description: ''
  name: 10Web Webhooks
  slug: 10web-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/10web-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/10web-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://10web.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.10web.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.10web.io/hc/en-us/articles/27304964365586-Introduction-to-10Web-API
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.10web.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://10web.io/website-builder-api/
- group: start
  title: ''
  type: SignUp
  url: https://my.10web.io/login
- group: operate
  title: ''
  type: Support
  url: https://help.10web.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://10web.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://10web.io/pricing/
- group: operate
  title: ''
  type: Roadmap
  url: https://help.10web.notion.site/10web-ai-builder-public-roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.10web.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://10web.io/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://10web.io/legal/privacy-policy/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/10web-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/10web-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/10web-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/10web-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/10web-lifecycle.yml
created: '2026-07-17'
description: 10Web is an AI-powered website builder platform that generates, hosts, and manages full WordPress websites on managed infrastructure, powering more than two million websites. Its public REST API — the 10Web Website Builder API (V1) — lets SaaS, agency, and hosting platforms embed 10Web's AI website generation, WordPress hosting, domains, DNS, SSL, backups, and staging as a white-label solution. The API exposes 69 operations across websites, AI/Vibe Coding content generation, domains and DNS zones, SSL certificates, backups, cache and PHP management, subdomains, the page builder, and signed webhooks, all authenticated with an x-api-key header against https://api.10web.io. Originally added to the API Evangelist network as a Sierra Ventures portfolio lead, this profile has been enriched from 10Web's public developer surface.
image: https://10web.io/wp-content/uploads/2025/03/OG-img4.jpg
layout: provider
mcp_servers:
- description: ''
  name: 10web-mcp.yml
  slug: 10web-mcpyml
modified: '2026-07-17'
name: 10Web
nav: Providers
network: true
overview: '10Web publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Backup API, Builder API, and 10 more. Tagged areas include Company, Ai, Website Builder, WordPress, and Hosting.


  The 10Web catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  10Web''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 55
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.9
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/10web/refs/heads/main/screenshots/10web-2026-07-25T181101.png
security:
- kind: authentication
  name: 10Web Authentication
  slug: 10web-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 10Web Domain Security
  slug: 10web-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 10web
tags:
- Company
- Ai
- Website Builder
- WordPress
- Hosting
- Website Generation
- No-Code
website: https://10web.io/
---
