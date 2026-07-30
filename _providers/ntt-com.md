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
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Unified API gateway for NTT Communications / NTT DOCOMO BUSINESS enterprise services. Catalogs APIs across Network, Cloud, Voice, App, Management, and Core categories — including Arcstar Universal One
  name: NTT DOCOMO BUSINESS Developer Portal
  slug: ntt-communications-developer-portal
- description: NTT Communications' Enterprise Cloud 2.0 control APIs for provisioning compute, storage, networking, and managed services. Programmatic access is provided via the eclsdk Python SDK, eclcloud Go SDK, t
  name: Smart Data Platform — Enterprise Cloud 2.0
  slug: smart-data-platform-cloud
- description: Network control APIs for NTT Communications' Flexible InterConnect service, enabling programmatic management of inter-cloud and inter-DC connectivity. Exposed through the terraform-provider-fic Terraf
  name: Smart Data Platform — Flexible InterConnect
  slug: smart-data-platform-network
- description: IoT device-management platform exposing a documented OpenAPI specification for device, measurement, alarm, event, and tenant management. Targets industrial and enterprise IoT deployments.
  name: NTT Communications Things Cloud
  slug: things-cloud
- description: 'Family of APIs for NTT Communications'' Arcstar Universal One managed VPN/network service — including traffic and contract info, circuit alarm retrieval, Flexible-Ethernet bandwidth and route control, '
  name: Arcstar Universal One APIs
  slug: arcstar-universal-one
- description: NTT DOCOMO's developer portal for smartphone-application APIs, launched November 2013. Provides API keys, console, and developer account management for DOCOMO services targeted at mobile-app builders.
  name: docomo Developer Support
  slug: docomo-developer-support
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ntt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://group.ntt/en/
- group: company
  title: ''
  type: Website
  url: https://www.global.ntt/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ntt.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.smt.docomo.ne.jp/
- group: other
  title: ''
  type: SmartDataPlatform
  url: https://sdpf.ntt.com/
- group: other
  title: ''
  type: NTTDocomo
  url: https://www.docomo.ne.jp/english/
- group: other
  title: ''
  type: NTTCommunications
  url: https://www.ntt.com/en.html
- group: other
  title: ''
  type: NTTDATA
  url: https://www.nttdata.com/global/en/
- group: other
  title: ''
  type: NTTLtd
  url: https://services.global.ntt/
- group: other
  title: ''
  type: NTTResearch
  url: https://ntt-research.com/
- group: other
  title: ''
  type: IOWN
  url: https://group.ntt/en/newsrelease/iown/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nttcom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NTTDATA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NTTDATA-EMEA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NTTDATA-DACH
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NTTDATAInnovation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/launchbynttdata
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nttdata-oss
- group: operate
  title: ''
  type: PressReleases
  url: https://group.ntt/en/newsrelease/
- group: company
  title: ''
  type: Careers
  url: https://group.ntt/en/careers/
- group: other
  title: ''
  type: Sustainability
  url: https://group.ntt/en/csr/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ntt/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/NTTGlobal
created: '2026-05-25'
description: NTT (Nippon Telegraph and Telephone Corporation) is a Tokyo-headquartered global technology and telecommunications group with roughly 340,000 employees and a 150-year history of innovation. The group operates through five business divisions — Consulting & IT Services, Mobile Solutions, Smart Tech, Consumer & Business, and Research & Development — and is anchored by major subsidiaries including NTT DOCOMO (Japan's largest mobile carrier), NTT Communications / NTT DOCOMO BUSINESS (enterprise cloud, network, and platform services), NTT DATA Group (global IT services and systems integration), NTT Ltd. (managed services), and NTT Research. NTT exposes a substantial developer surface through the NTT DOCOMO BUSINESS Developer Portal at developer.ntt.com, which catalogs enterprise APIs across Network (Arcstar Universal One, Flexible InterConnect, Global M2M), Cloud (Smart Data Platform, Enterprise Cloud 2.0), Voice, App (Safety Confirmation, Text & Language Analysis, Speech Recognition),
  Management (asset visibility, vulnerability), and Core (Authorization, Billing, API Log, Business Process, Service Order, Pay-per-use, Price, Organization, Personal Profile) categories. The group also publishes IoT APIs (Things Cloud) and a docomo Developer support portal at dev.smt.docomo.ne.jp. NTT's primary open source presence is the nttcom GitHub organization, which ships the Enterprise Cloud Python and Go SDKs (eclsdk / eclcloud), the eclcli command-line tool, Terraform providers for Enterprise Cloud 2.0 (terraform-provider- ecl) and Flexible InterConnect (terraform-provider-fic), the ksot network-IaC framework, the pola stateful PCE / PCEP library, the fluvia eBPF/XDP IPFIX exporter, and threatconnectome for SBOM-driven vulnerability management. NTT DATA additionally maintains regional GitHub orgs (NTTDATA, NTTDATA-EMEA, NTTDATA-DACH, NTTDATAInnovation, launchbynttdata, nttdata-oss) covering testing automation, Kubernetes plugins, and LLM observability tooling. NTT also drives the
  IOWN (Innovative Optical and Wireless Network) initiative, photonics and optical-quantum research, and responsible AI development across its R&D arm.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ntt-com.png
layout: provider
modified: '2026-05-25'
name: NTT
nav: Providers
network: true
overview: 'NTT publishes 1 API on the [APIs.io](https://apis.io/) network: Communications Things Cloud. Tagged areas include Telecommunications, Mobile Networks, Enterprise Cloud, Smart Data Platform, and IOWN.


  NTT''s developer surface includes YouTube channel and 23 more developer resources.'
random_paper: 50
score:
  band: emerging
  composite: 15.7
  delta: -4.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ntt-com/refs/heads/main/screenshots/ntt-com-2026-06-20T190459.png
security:
- kind: domain-security
  name: Ntt Com Domain Security
  slug: ntt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ntt-com
tags:
- Telecommunications
- Mobile Networks
- Enterprise Cloud
- Smart Data Platform
- IOWN
- 5G
- IoT
- Things Cloud
- Network APIs
- SD-WAN
- Photonics
- Japan
- Systems Integration
website: https://group.ntt/en/
---
