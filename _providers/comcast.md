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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Firebolt is Comcast's application platform for building apps that run on TVs, set-top boxes, and other connected home devices. The Firebolt SDK exposes a family of JavaScript APIs (Lifecycle, Metrics,
  name: Comcast Firebolt SDK
  slug: firebolt-sdk
- description: The Comcast Security Access Token (SAT) endpoint issues short-lived bearer tokens used to authenticate calls to Comcast partner APIs such as the Open Ingest service. Clients exchange an x-client-id an
  name: Comcast Authentication API (SAT)
  slug: authentication-api
- description: The Comcast Open Ingest endpoint accepts metadata and content asset packages from NBCUniversal media partners. Clients POST an XML payload describing assets to the Merlin ingest proxy, authenticated w
  name: Comcast Open Ingest API
  slug: open-ingest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/comcast-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/comcast
- group: company
  title: ''
  type: Website
  url: https://www.comcast.com
- group: docs
  title: ''
  type: DeveloperDocs
  url: https://docs.developer.comcast.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.comcast.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Comcast
- group: other
  title: ''
  type: OpenSource
  url: https://comcast.github.io/
- group: other
  title: ''
  type: Xfinity
  url: https://www.xfinity.com/
- group: other
  title: ''
  type: NBCUniversal
  url: https://www.nbcuniversal.com/
- group: company
  title: ''
  type: Investors
  url: https://www.cmcsa.com/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.xfinity.com/privacy/policy
- group: commercial
  title: ''
  type: Terms
  url: https://developers.xfinity.com/TOS.html
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.comcast.com/llms.txt
created: '2026-03-21'
description: Comcast Corporation is a global media and technology company with two primary businesses, Comcast Cable (Xfinity) and NBCUniversal, providing video, internet, voice, wireless, and entertainment services to residential and business customers. Comcast publishes a public developer program centered on the Firebolt application platform for connected TV experiences, along with authentication and content ingest endpoints used by NBCUniversal media partners. The Firebolt SDK family is used by app developers to write apps once and deploy across Xfinity X1, Xfinity Flex, Sky Q, and other Comcast set-top boxes and connected devices.
finops:
- name: Comcast Finops
  service_category: Telecommunications
  slug: comcast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/comcast.png
layout: provider
modified: '2026-04-26'
name: Comcast
nav: Providers
network: true
overview: 'Comcast publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cable, Connected Devices, Entertainment, Internet, and Media.


  Comcast''s developer surface includes GitHub presence, privacy policy, terms of service, and 10 more developer resources.'
plans:
- name: Comcast Plans Pricing
  plan_count: 1
  slug: comcast-plans-pricing
press:
- date: '2026-05-25'
  title: How Comcast Used AI and Unified Search to Transform ...
  url: https://www.coveo.com/blog/comcast-employee-experience/
- date: '2026-05-25'
  title: Comcast Technology Solutions' VideoAI™ Integrated with ...
  url: https://www.prnewswire.com/news-releases/comcast-technology-solutions-videoai-integrated-with-orange-logic-marketplace-for-ai-powered-management-of-video-assets-and-metadata-302448471.html
- date: '2026-05-25'
  title: Comcast Pushes AI to the Edge to Power the Nation's ...
  url: https://corporate.comcast.com/press/releases/comcast-pushes-ai-to-the-edge-to-power-the-nations-smartest-broadband-network
- date: '2026-05-25'
  title: Comcast Advertising Introduces New AI Platform to Help ...
  url: https://comcastadvertising.com/news/comcast-advertising-introduces-new-ai-platform-to-help-small-and-local-businesses-create-cost-effective-commercials-in-minutes/
- date: '2026-05-25'
  title: 'Comcast''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/comcast-ai-strategy-analysis-of-dominance-in-telecommunications-and-media/
random_paper: 35
rate_limits:
- limit_count: 1
  name: Comcast Rate Limits
  slug: comcast-rate-limits
score:
  band: emerging
  composite: 19.5
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/comcast/refs/heads/main/screenshots/comcast-2026-06-20T174802.png
security:
- kind: domain-security
  name: Comcast Domain Security
  slug: comcast-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: comcast
tags:
- Cable
- Connected Devices
- Entertainment
- Internet
- Media
- Mobile
- Streaming
- Wireless
- Fortune 100
website: https://www.comcast.com
---
