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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Wireshark is a free and open-source network protocol analyzer that captures and interactively browses network traffic. It supports hundreds of protocols, runs on multiple platforms, and provides deep '
  name: Wireshark
  slug: wireshark
artifact_total: 24
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wireshark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wireshark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wireshark.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.wireshark.org/docs/
- group: company
  title: ''
  type: Blog
  url: https://blog.wireshark.org
- group: operate
  title: ''
  type: FAQ
  url: https://www.wireshark.org/faq.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wireshark/wireshark
- group: build
  title: ''
  type: GitLab
  url: https://gitlab.com/wireshark/wireshark
- group: operate
  title: ''
  type: Support
  url: https://ask.wireshark.org
- group: other
  title: ''
  type: Downloads
  url: https://www.wireshark.org/download.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.wireshark.org/docs/relnotes/
- group: operate
  title: ''
  type: Forums
  url: https://www.wireshark.org/lists/
created: '2025-01-08'
description: Wireshark is the world's foremost and widely-used free and open-source network protocol analyzer. It lets you capture and interactively browse the traffic running on a computer network. Wireshark provides a powerful dissector framework with a Lua scripting API, C/C++ plugin architecture, TShark command-line tools, and the libwireshark library for developers building network analysis tools.
features:
- description: Capture live network traffic from multiple interfaces simultaneously using libpcap/Npcap.
  name: Packet Capture
- description: Analyze hundreds of protocols with full decode of packet fields and values.
  name: Deep Packet Inspection
- description: Powerful filter language for drilling into captured traffic.
  name: Display Filters
- description: Extend Wireshark with custom dissectors, listeners, and menus using the Lua API.
  name: Lua Scripting
- description: Write C/C++ plugins to add support for new protocols.
  name: Dissector Plugins
- description: Command-line version of Wireshark for scripting and automation.
  name: TShark CLI
- description: Plugin API to add custom capture sources to Wireshark.
  name: Extcap Interface
- description: Library for reading and writing capture file formats including pcap and pcapng.
  name: Wiretap Library
finops:
- name: Wireshark Finops
  service_category: API
  slug: wireshark-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wireshark.png
integrations:
- description: Command-line packet analyzer that uses the same dissection engine as Wireshark.
  name: TShark
- description: Minimal capture utility used by Wireshark and TShark.
  name: dumpcap
- description: Utility for editing and converting capture files.
  name: editcap
- description: Scripting language embedded in Wireshark for custom protocol dissectors.
  name: Lua
- description: Packet capture libraries used by Wireshark on Unix and Windows respectively.
  name: libpcap/Npcap
layout: provider
modified: '2026-05-03'
name: Wireshark
nav: Providers
network: true
overview: 'Wireshark publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Debugging, Network Analysis, Open-Source, Packet Capture, and Protocol Analysis.


  Wireshark''s developer surface includes documentation, engineering blog, FAQ, GitHub presence, support, release notes, and 6 more developer resources.'
plans:
- name: Wireshark Plans Pricing
  plan_count: 3
  slug: wireshark-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Wireshark Rate Limits
  slug: wireshark-rate-limits
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 21.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wireshark/refs/heads/main/screenshots/wireshark-2026-06-20T201522.png
security:
- kind: domain-security
  name: Wireshark Domain Security
  slug: wireshark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wireshark Vulnerability Disclosure
  slug: wireshark-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wireshark
tags:
- Debugging
- Network Analysis
- Open-Source
- Packet Capture
- Protocol Analysis
- Security
use_cases:
- description: Diagnose latency, packet loss, and protocol errors in live or captured traffic.
  name: Network Troubleshooting
- description: Inspect raw HTTP, gRPC, and WebSocket API requests and responses at the packet level.
  name: API Traffic Debugging
- description: Develop and test new network protocols using Wireshark dissectors.
  name: Protocol Development
- description: Analyze network traffic for intrusion indicators and malicious patterns.
  name: Security Analysis
- description: Learn networking concepts by capturing and examining real protocol exchanges.
  name: Education
website: https://www.wireshark.org
---
