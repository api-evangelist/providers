---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'ARRIS Group publishes no API. The entry is retained to record the measurement: probed 2026-09-07, no OpenAPI, Swagger, AsyncAPI, GraphQL SDL, MCP endpoint, agent card or Postman collection was found o'
  name: ARRIS Group Developer Surface
  slug: commscope-api
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.commscope.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arris-group-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.commscope.com/blog/rss/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arris
- group: start
  title: CommScope Website (formerly ARRIS)
  type: Portal
  url: https://www.commscope.com/
- group: docs
  title: Solutions
  type: Documentation
  url: https://www.commscope.com/solutions/
- group: operate
  title: Support
  type: Support
  url: https://www.commscope.com/support/
- group: build
  title: ARRIS-Group on GitHub
  type: GitHubOrganization
  url: https://github.com/ARRIS-Group
- group: agent
  title: llms.txt for ARRIS Group
  type: LLMsTxt
  url: llms/arris-group-llms.txt
coverage:
  checked: '2026-09-07'
  detail: 'ARRIS Group stopped existing as a publisher in 2019 when CommScope absorbed it, and the trail ends twice more since: CommScope sold the ex-ARRIS Home Networks unit to Vantiva in 2023 and renamed itself Vistance Networks in January 2026, so arris.com and arrisi.com now 301 straight to www.vistancenetworks.com while developer.arris.com, api.arris.com and support.arris.com return NXDOMAIN.'
  evidence:
  - status: 301
    url: https://www.arris.com/
  - status: 404
    url: https://www.commscope.com/.well-known/api-catalog
  - status: 404
    url: https://www.commscope.com/openapi.json
  - status: 404
    url: https://www.vistancenetworks.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/ARRIS-Group
  reason: defunct
  state: none
created: '2024-12-03'
description: ARRIS Group was a global telecommunications equipment company providing entertainment and communications solutions including broadband, video, and wireless products for service providers and consumers. ARRIS was acquired by CommScope in 2019, combining their broadband technology expertise with CommScope's infrastructure solutions. The combined company offers cable modem equipment, set-top boxes, network infrastructure, DOCSIS technology, and related telecommunications hardware and software platforms for cable operators, telcos, and internet service providers worldwide.
features:
- description: ARRIS/CommScope provides Data Over Cable Service Interface Specification (DOCSIS) technology enabling high-speed internet over cable infrastructure, including DOCSIS 3.1 and 3.0 modems and gateways.
  name: DOCSIS Technology
- description: Advanced set-top box products for cable operators enabling video delivery, content access, and interactive television services.
  name: Set-Top Box Platform
- description: Software platforms for managing broadband access networks, including CMTS (Cable Modem Termination System) management and network analytics.
  name: Network Infrastructure Management
- description: Converged Cable Access Platform technology converging CMTS and video-on-demand processing into a single platform.
  name: CCAP Architecture
finops:
- name: Arris Group Finops
  service_category: API
  slug: arris-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arris-group.png
integrations:
- description: ARRIS equipment integrates with CableLabs DOCSIS standards for interoperability across cable plant vendors and operators.
  name: DOCSIS Standards
- description: Integration with Society of Cable Telecommunications Engineers (SCTE) standards for cable network operations and maintenance.
  name: SCTE Standards
layout: provider
modified: '2026-09-07'
name: ARRIS Group
nav: Providers
network: true
overview: 'ARRIS Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Broadband, Cable, Video, and Networking.


  ARRIS Group''s developer surface includes engineering blog, developer portal, documentation, support, and 5 more developer resources.'
plans:
- name: Arris Group Plans Pricing
  plan_count: 0
  slug: arris-group-plans-pricing
press:
- date: '2026-05-25'
  title: Will Comcast Abandon ARRIS Group for Apple?
  url: https://www.fool.com/investing/general/2014/03/24/will-comcast-abandon-arris-group-for-apple.aspx
- date: '2026-05-25'
  title: ARRIS Completes Pace Acquisition
  url: https://www.prnewswire.com/news-releases/arris-completes-pace-acquisition-300198914.html
- date: '2026-05-25'
  title: ARRIS Group Major Strategic Acquisition, eBay Quarterly ...
  url: https://www.gurufocus.com/news/332164/arris-group-major-strategic-acquisition-ebay-quarterly-profit-above-consensus?mobile=true%3Fmobile%3Dtrue&mobile=true%3Fmobile%3Dtrue%3Fmobile%3Dtrue&mobile=true&mobile=true
- date: '2026-05-25'
  title: Google Sells Motorola Home to Arris Group for $2.35 Billion
  url: https://www.datamation.com/trends/google-sells-motorola-home-to-arris-group-for-2-35-billion/
- date: '2026-05-25'
  title: Arris Wins 4K STB Deal With Altice
  url: https://www.lightreading.com/network-technology/arris-wins-4k-stb-deal-with-altice
random_paper: 13
rate_limits:
- limit_count: 0
  name: Arris Group Rate Limits
  slug: arris-group-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/arris-group/refs/heads/main/screenshots/arris-group-2026-06-20T172437.png
security:
- kind: domain-security
  name: Arris Group Domain Security
  slug: arris-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arris-group
tags:
- Telecommunications
- Broadband
- Cable
- Video
- Networking
- Equipment
use_cases:
- description: Cable operators use ARRIS/CommScope equipment to deploy and manage broadband internet infrastructure for residential and business customers.
  name: Broadband Network Deployment
- description: Television service providers use ARRIS set-top boxes and headend equipment to deliver linear and on-demand video content to subscribers.
  name: Video Service Delivery
- description: Network operations teams use management software to monitor, configure, and troubleshoot broadband access networks and cable plant equipment.
  name: Network Operations
website: https://www.commscope.com/
---
