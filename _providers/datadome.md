---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Datadome Agentic Access
  operation_count: 31
  slug: datadome-agentic-access
  summary_line: 31 operations · 17 acting
api_count: 17
apis:
- description: Bot Protect is DataDome's core bot management product, scoring every request against the platform's threat intelligence and machine-learning models to classify and block automated traffic (scraping, c
  name: DataDome Bot Protect
  slug: bot-protect
- description: Account Protect targets account takeover, fake account creation, and post-login abuse using behavioral, device, and credential signals layered on top of the Bot Protect decisioning core.
  name: DataDome Account Protect
  slug: account-protect
- description: Ad Protect filters invalid traffic from ad-supported properties and protects publishers and advertisers from automated click and impression fraud, leveraging the same signal pipeline as Bot Protect.
  name: DataDome Ad Protect
  slug: ad-protect
- description: Page Protect provides client-side security and Magecart / formjacking defense, inventorying third-party scripts and detecting unauthorized data exfiltration from sensitive pages such as checkout and a
  name: DataDome Page Protect
  slug: page-protect
- description: Agentic Trust is DataDome's product for managing AI-agent traffic, letting customers identify, authenticate, and govern interactions from autonomous agents and LLM-driven crawlers against their web an
  name: DataDome Agentic Trust
  slug: agentic-trust
- description: DDoS Protect mitigates application-layer denial-of-service attacks using the same edge-distributed signal pipeline as Bot Protect, defending APIs and web properties against high-volume automated campa
  name: DataDome DDoS Protect
  slug: ddos-protect
- description: The DataDome JS tag collects browser, device, and behavioral signals that are forwarded to the DataDome decisioning service. The tag is configured per property and loaded asynchronously to avoid impac
  name: DataDome JavaScript Tag
  slug: js-tag
- description: DataDome ships 40+ server-side integrations (web servers, CDNs, application frameworks, API gateways) that forward each request to the DataDome decisioning service and apply the returned verdict. Thes
  name: DataDome Server Modules & SDKs
  slug: server-modules
- description: Native iOS and Android SDKs (with React Native and Flutter wrappers) integrate with common HTTP libraries (OkHttp, Alamofire, Axios, Dio) so DataDome verdicts can be applied to mobile API traffic, not
  name: DataDome Mobile SDKs
  slug: mobile-sdks
- description: The Account API from DataDome — 4 operation(s) for account.
  name: DataDome Account API
  slug: datadome-account-api
- description: The AccountProtect API from DataDome — 1 operation(s) for accountprotect.
  name: DataDome AccountProtect API
  slug: datadome-accountprotect-api
- description: The CustomRules API from DataDome — 2 operation(s) for customrules.
  name: DataDome CustomRules API
  slug: datadome-customrules-api
- description: The Endpoints API from DataDome — 2 operation(s) for endpoints.
  name: DataDome Endpoints API
  slug: datadome-endpoints-api
- description: The Priorities API from DataDome — 3 operation(s) for priorities.
  name: DataDome Priorities API
  slug: datadome-priorities-api
- description: The Templates API from DataDome — 2 operation(s) for templates.
  name: DataDome Templates API
  slug: datadome-templates-api
- description: The TrustedProxies API from DataDome — 2 operation(s) for trustedproxies.
  name: DataDome TrustedProxies API
  slug: datadome-trustedproxies-api
- description: The VerifiedModels API from DataDome — 1 operation(s) for verifiedmodels.
  name: DataDome VerifiedModels API
  slug: datadome-verifiedmodels-api
artifact_total: 24
collections:
- collection_type: open
  name: DataDome Management API
  slug: open-datadome
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datadome-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datadome-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datadome-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://datadome.co/
- group: other
  title: ''
  type: Products
  url: https://datadome.co/products/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datadome.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.datadome.co/reference
- group: company
  title: ''
  type: Blog
  url: https://datadome.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataDome
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datadome/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/datadome
- group: operate
  title: ''
  type: Status
  url: https://status.datadome.co/
- group: operate
  title: ''
  type: Contact
  url: https://datadome.co/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.datadome.co/llms.txt
created: '2026-05-23'
description: DataDome is a real-time bot and online fraud protection platform that inspects every web, mobile, and API request and decides — within milliseconds — whether it should be allowed, challenged, or blocked. The platform combines a JavaScript tag and mobile SDKs (iOS, Android, React Native, Flutter) on the client side with 40+ server-side integrations (Nginx, Apache, IIS, OpenResty, HAProxy, Cloudflare Workers, AWS CloudFront, Fastly, Bunny, Node.js, Python ASGI, Go, Ruby, Java, ASP.NET Core, Kong, Apigee, Tyk, Traefik) that forward signals to DataDome's decisioning service. Products in the platform include Bot Protect, Account Protect, Ad Protect, Page Protect, Priority Protect, Agentic Trust (governing AI agent traffic), and DDoS Protect.
finops:
- name: Datadome Finops
  service_category: API
  slug: datadome-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datadome.png
layout: provider
modified: '2026-05-23'
name: DataDome
nav: Providers
network: true
overview: 'DataDome publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, AccountProtect API, CustomRules API, and 5 more. Tagged areas include Bot Mitigation, Fraud Protection, Account Protection, Ad Fraud, and DDoS.


  DataDome''s developer surface includes authentication, documentation, API reference, engineering blog, status page, and 9 more developer resources.'
plans:
- name: Datadome Plans Pricing
  plan_count: 1
  slug: datadome-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Datadome Rate Limits
  slug: datadome-rate-limits
score:
  band: thin
  composite: 32.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 44.2
    developer_ergonomics: 28.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datadome/refs/heads/main/screenshots/datadome-2026-06-20T175642.png
security:
- kind: authentication
  name: Datadome Authentication
  slug: datadome-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Datadome Domain Security
  slug: datadome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datadome
tags:
- Bot Mitigation
- Fraud Protection
- Account Protection
- Ad Fraud
- DDoS
- Real-Time
- Edge Security
- Application Security
- Agentic Trust
website: https://datadome.co/
---
