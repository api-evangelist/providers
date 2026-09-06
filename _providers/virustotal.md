---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 56
  human_in_the_loop: 11
  name: Virustotal Agentic Access
  operation_count: 206
  slug: virustotal-agentic-access
  summary_line: 206 operations · 56 acting · 11 human-in-the-loop
api_count: 7
apis:
- description: Enterprise add-on (formerly Mandiant Advantage ASM). Discovers and monitors an organisation's external attack surface, scoring exposures and prioritising remediation.
  name: Google Threat Intelligence - Attack Surface Management (ASM)
  slug: google-threat-intelligence-attack-surface-management-asm
- description: Enterprise add-on (formerly Mandiant Advantage DTM). Monitors the open, deep, and dark web for credential leaks, brand abuse, and adversary chatter referencing the customer.
  name: Google Threat Intelligence - Digital Threat Monitoring (DTM)
  slug: google-threat-intelligence-digital-threat-monitoring-dtm
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Access Control - Group Management
  name: VirusTotal Access Control - Group Management API
  slug: virustotal-access-control-group-management-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Access Control - Quota Management
  name: VirusTotal Access Control - Quota Management API
  slug: virustotal-access-control-quota-management-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Access Control - Service Account Management
  name: VirusTotal Access Control - Service Account Management API
  slug: virustotal-access-control-service-account-management-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Access Control - User Management
  name: VirusTotal Access Control - User Management API
  slug: virustotal-access-control-user-management-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Feeds - Domain intelligence feed
  name: VirusTotal IoC Feeds - Domain intelligence feed API
  slug: virustotal-ioc-feeds-domain-intelligence-feed-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Feeds - File intelligence feed
  name: VirusTotal IoC Feeds - File intelligence feed API
  slug: virustotal-ioc-feeds-file-intelligence-feed-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Feeds - IP intelligence feed
  name: VirusTotal IoC Feeds - IP intelligence feed API
  slug: virustotal-ioc-feeds-ip-intelligence-feed-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Feeds - Sandbox analyses feed
  name: VirusTotal IoC Feeds - Sandbox analyses feed API
  slug: virustotal-ioc-feeds-sandbox-analyses-feed-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Feeds - URL intelligence feed
  name: VirusTotal IoC Feeds - URL intelligence feed API
  slug: virustotal-ioc-feeds-url-intelligence-feed-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Analyses, Submissions & Operations
  name: VirusTotal IoC Investigation - Analyses, Submissions & Operations API
  slug: virustotal-ioc-investigation-analyses-submissions-operations-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Attack Tactics
  name: VirusTotal IoC Investigation - Attack Tactics API
  slug: virustotal-ioc-investigation-attack-tactics-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Attack Techniques
  name: VirusTotal IoC Investigation - Attack Techniques API
  slug: virustotal-ioc-investigation-attack-techniques-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Comments
  name: VirusTotal IoC Investigation - Comments API
  slug: virustotal-ioc-investigation-comments-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Domains & Resolutions
  name: VirusTotal IoC Investigation - Domains & Resolutions API
  slug: virustotal-ioc-investigation-domains-resolutions-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Files
  name: VirusTotal IoC Investigation - Files API
  slug: virustotal-ioc-investigation-files-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Files Behaviours
  name: VirusTotal IoC Investigation - Files Behaviours API
  slug: virustotal-ioc-investigation-files-behaviours-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - IP addresses
  name: VirusTotal IoC Investigation - IP addresses API
  slug: virustotal-ioc-investigation-ip-addresses-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Popular Threat Categories
  name: VirusTotal IoC Investigation - Popular Threat Categories API
  slug: virustotal-ioc-investigation-popular-threat-categories-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Search & Metadata
  name: VirusTotal IoC Investigation - Search & Metadata API
  slug: virustotal-ioc-investigation-search-metadata-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - URLs
  name: VirusTotal IoC Investigation - URLs API
  slug: virustotal-ioc-investigation-urls-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: IoC Investigation - Zipping files
  name: VirusTotal IoC Investigation - Zipping files API
  slug: virustotal-ioc-investigation-zipping-files-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Private Scanning - Analyses
  name: VirusTotal Private Scanning - Analyses API
  slug: virustotal-private-scanning-analyses-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Private Scanning - Files
  name: VirusTotal Private Scanning - Files API
  slug: virustotal-private-scanning-files-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Private Scanning - Files Behaviours
  name: VirusTotal Private Scanning - Files Behaviours API
  slug: virustotal-private-scanning-files-behaviours-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Private Scanning - URLs
  name: VirusTotal Private Scanning - URLs API
  slug: virustotal-private-scanning-urls-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Private Scanning - Zipping files
  name: VirusTotal Private Scanning - Zipping files API
  slug: virustotal-private-scanning-zipping-files-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Threat Graphs
  name: VirusTotal Threat Graphs API
  slug: virustotal-threat-graphs-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Threat Graphs Permissions & ACL
  name: VirusTotal Threat Graphs Permissions & ACL API
  slug: virustotal-threat-graphs-permissions-acl-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: Threat Landscape & Vulnerability Intelligence & Reports & Analysis
  name: VirusTotal Threat Landscape & Vulnerability Intelligence & Reports & Analysis API
  slug: virustotal-threat-landscape-vulnerability-intelligence-reports-analysis-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: YARA Hunting - IoC Stream
  name: VirusTotal YARA Hunting - IoC Stream API
  slug: virustotal-yara-hunting-ioc-stream-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: YARA Hunting - Livehunt
  name: VirusTotal YARA Hunting - Livehunt API
  slug: virustotal-yara-hunting-livehunt-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: YARA Hunting - Retrohunt
  name: VirusTotal YARA Hunting - Retrohunt API
  slug: virustotal-yara-hunting-retrohunt-api
- baseURL: https://www.virustotal.com/api/v3
  baseurl_source: declared
  description: YARA Hunting - Rules
  name: VirusTotal YARA Hunting - Rules API
  slug: virustotal-yara-hunting-rules-api
artifact_total: 142
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management API
  slug: open-virustotal-access-control-group-management-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Access Control - Quota Management API
  slug: open-virustotal-access-control-quota-management-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Access Control - Service Account Management API
  slug: open-virustotal-access-control-service-account-management-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Access Control - User Management API
  slug: open-virustotal-access-control-user-management-api
- collection_type: open
  name: VirusTotal API v3 - Access Control
  slug: open-virustotal-access-control
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Feeds - Domain intelligence feed API
  slug: open-virustotal-ioc-feeds-domain-intelligence-feed-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Feeds - File intelligence feed API
  slug: open-virustotal-ioc-feeds-file-intelligence-feed-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Feeds - IP intelligence feed API
  slug: open-virustotal-ioc-feeds-ip-intelligence-feed-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Feeds - Sandbox analyses feed API
  slug: open-virustotal-ioc-feeds-sandbox-analyses-feed-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Feeds - URL intelligence feed API
  slug: open-virustotal-ioc-feeds-url-intelligence-feed-api
- collection_type: open
  name: VirusTotal API v3 - IoC Feeds
  slug: open-virustotal-ioc-feeds
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Analyses, Submissions & Operations API
  slug: open-virustotal-ioc-investigation-analyses-submissions-operations-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Attack Tactics API
  slug: open-virustotal-ioc-investigation-attack-tactics-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Attack Techniques API
  slug: open-virustotal-ioc-investigation-attack-techniques-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Comments API
  slug: open-virustotal-ioc-investigation-comments-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Domains & Resolutions API
  slug: open-virustotal-ioc-investigation-domains-resolutions-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Files API
  slug: open-virustotal-ioc-investigation-files-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Files Behaviours API
  slug: open-virustotal-ioc-investigation-files-behaviours-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - IP addresses API
  slug: open-virustotal-ioc-investigation-ip-addresses-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Popular Threat Categories API
  slug: open-virustotal-ioc-investigation-popular-threat-categories-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Search & Metadata API
  slug: open-virustotal-ioc-investigation-search-metadata-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - URLs API
  slug: open-virustotal-ioc-investigation-urls-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management IoC Investigation - Zipping files API
  slug: open-virustotal-ioc-investigation-zipping-files-api
- collection_type: open
  name: VirusTotal API v3 - IoC Investigation
  slug: open-virustotal-ioc-investigation
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Private Scanning - Analyses API
  slug: open-virustotal-private-scanning-analyses-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Private Scanning - Files API
  slug: open-virustotal-private-scanning-files-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Private Scanning - Files Behaviours API
  slug: open-virustotal-private-scanning-files-behaviours-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Private Scanning - URLs API
  slug: open-virustotal-private-scanning-urls-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Private Scanning - Zipping files API
  slug: open-virustotal-private-scanning-zipping-files-api
- collection_type: open
  name: VirusTotal API v3 - Private Scanning
  slug: open-virustotal-private-scanning
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Threat Graphs API
  slug: open-virustotal-threat-graphs-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Threat Graphs Permissions & ACL API
  slug: open-virustotal-threat-graphs-permissions-acl-api
- collection_type: open
  name: VirusTotal API v3 - Threat Graphs
  slug: open-virustotal-threat-graphs
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management Threat Landscape & Vulnerability Intelligence & Reports & Analysis API
  slug: open-virustotal-threat-landscape-vulnerability-intelligence-reports-analysis-api
- collection_type: open
  name: VirusTotal API v3 - Threat Landscape and Vulnerability Intelligence
  slug: open-virustotal-threat-landscape
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management YARA Hunting - IoC Stream API
  slug: open-virustotal-yara-hunting-ioc-stream-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management YARA Hunting - Livehunt API
  slug: open-virustotal-yara-hunting-livehunt-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management YARA Hunting - Retrohunt API
  slug: open-virustotal-yara-hunting-retrohunt-api
- collection_type: open
  name: VirusTotal API v3 - Access Control Access Control - Group Management YARA Hunting - Rules API
  slug: open-virustotal-yara-hunting-rules-api
- collection_type: open
  name: VirusTotal API v3 - YARA Hunting (Livehunt, Retrohunt, IoC Stream)
  slug: open-virustotal-yara-hunting
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/virustotal-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virustotal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virustotal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virustotal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.virustotal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virustotal.com/reference/overview
- group: docs
  title: ''
  type: APIReference
  url: https://gtidocs.virustotal.com/reference/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VirusTotal
- group: company
  title: ''
  type: Blog
  url: https://blog.virustotal.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: docs
  title: GTI API v3 — Full Spec (official, upstream)
  type: OpenAPI
  url: https://storage.googleapis.com/gtidocresources/guides/GTI_API_v3_openapi_spec_10022025.json
- group: docs
  title: GTI ASM — Attack Surface Management
  type: OpenAPI
  url: https://gtidocs.virustotal.com/openapi/asm-attack-surface-management.json
- group: docs
  title: GTI DTM — Digital Threat Monitoring
  type: OpenAPI
  url: https://gtidocs.virustotal.com/openapi/dtm-digital-threat-monitoring.json
- group: build
  title: Python SDK (vt-py)
  type: SDKs
  url: https://github.com/VirusTotal/vt-py
- group: build
  title: Go SDK (vt-go)
  type: SDKs
  url: https://github.com/VirusTotal/vt-go
- group: build
  title: Graph API Python (vt-graph-api)
  type: SDKs
  url: https://github.com/VirusTotal/vt-graph-api
- group: build
  title: vt-cli — Official VirusTotal Command Line Interface (Go)
  type: CLI
  url: https://github.com/VirusTotal/vt-cli
- group: build
  title: MCP Server (BurtTheCoder/mcp-virustotal — community)
  type: Tools
  url: https://github.com/BurtTheCoder/mcp-virustotal
- group: build
  title: MCP Server (alephnan/MCP-VirusTotal — community)
  type: Tools
  url: https://github.com/alephnan/MCP-VirusTotal
- group: build
  title: MCP Server (barvhaim/virustotal-mcp-server — community, Python)
  type: Tools
  url: https://github.com/barvhaim/virustotal-mcp-server
- group: build
  title: YARA (the pattern matching swiss knife)
  type: Tools
  url: https://github.com/VirusTotal/yara
- group: build
  title: YARA-X (Rust rewrite of YARA)
  type: Tools
  url: https://github.com/VirusTotal/yara-x
- group: build
  title: yara-python (Python interface for YARA)
  type: Tools
  url: https://github.com/VirusTotal/yara-python
- group: build
  title: yara-x-benchmarks
  type: Tools
  url: https://github.com/VirusTotal/yara-x-benchmarks
- group: build
  title: go-yara (Go bindings for YARA)
  type: Tools
  url: https://github.com/VirusTotal/go-yara
- group: build
  title: protoc-gen-yara (YARA modules from protobufs)
  type: Tools
  url: https://github.com/VirusTotal/protoc-gen-yara
- group: build
  title: CAPEv2 (Malware Configuration And Payload Extraction)
  type: Tools
  url: https://github.com/VirusTotal/CAPEv2
- group: build
  title: vt-ida-plugin (Official VirusTotal plugin for IDA Pro)
  type: Tools
  url: https://github.com/VirusTotal/vt-ida-plugin
- group: build
  title: vt-windows-event-stream
  type: Tools
  url: https://github.com/VirusTotal/vt-windows-event-stream
- group: build
  title: qt-virustotal-uploader (Qt desktop uploader)
  type: Tools
  url: https://github.com/VirusTotal/qt-virustotal-uploader
- group: learn
  title: GTI Developer Kit (example integration code)
  type: Tutorials
  url: https://github.com/VirusTotal/gti-dev-kit
- group: commercial
  title: ''
  type: Plans
  url: plans/virustotal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virustotal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/virustotal-finops.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/virustotal-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/virustotal-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/virustotal-context.jsonld
created: '2026-05-28'
description: 'VirusTotal — the Google-owned (since 2012) threat intelligence platform that aggregates anti-malware engines and URL scanners to analyse files, URLs, IP addresses, and domains. The v3 API surfaces seven major areas: Access Control, IoC Feeds, IoC Investigation, Private Scanning, Threat Graphs, Threat Landscape & Vulnerability Intelligence, and YARA Hunting (Livehunt, Retrohunt, IoC Stream). Now also branded "Google Threat Intelligence" (GTI) for Enterprise customers, integrating Mandiant intelligence, Digital Threat Monitoring (DTM), and Attack Surface Management (ASM).'
examples:
- key_count: 5
  name: Virustotal Analysis Object Example
  slug: virustotal-analysis-object-example
- key_count: 5
  name: Virustotal Attack Tactic Object Example
  slug: virustotal-attack-tactic-object-example
- key_count: 5
  name: Virustotal Attack Technique Object Example
  slug: virustotal-attack-technique-object-example
- key_count: 5
  name: Virustotal Collection Object Example
  slug: virustotal-collection-object-example
- key_count: 5
  name: Virustotal Comment Object Example
  slug: virustotal-comment-object-example
- key_count: 5
  name: Virustotal Domain Object Example
  slug: virustotal-domain-object-example
- key_count: 5
  name: Virustotal File Behaviour Object Example
  slug: virustotal-file-behaviour-object-example
- key_count: 5
  name: Virustotal File Object Example
  slug: virustotal-file-object-example
- key_count: 5
  name: Virustotal Graph Object Example
  slug: virustotal-graph-object-example
- key_count: 5
  name: Virustotal Group Object Example
  slug: virustotal-group-object-example
- key_count: 5
  name: Virustotal Ioc Stream Notification Object Example
  slug: virustotal-ioc-stream-notification-object-example
- key_count: 5
  name: Virustotal Ip Address Object Example
  slug: virustotal-ip-address-object-example
- key_count: 5
  name: Virustotal Livehunt Ruleset Object Example
  slug: virustotal-livehunt-ruleset-object-example
- key_count: 5
  name: Virustotal Popular Threat Category Object Example
  slug: virustotal-popular-threat-category-object-example
- key_count: 5
  name: Virustotal Retrohunt Job Object Example
  slug: virustotal-retrohunt-job-object-example
- key_count: 5
  name: Virustotal Url Object Example
  slug: virustotal-url-object-example
- key_count: 5
  name: Virustotal User Object Example
  slug: virustotal-user-object-example
- key_count: 5
  name: Virustotal Vote Object Example
  slug: virustotal-vote-object-example
- key_count: 5
  name: Virustotal Yara Rule Object Example
  slug: virustotal-yara-rule-object-example
finops:
- name: Virustotal Finops
  service_category: Threat Intelligence
  slug: virustotal-finops
image: https://www.virustotal.com/gui/images/vt-logo.svg
json_schemas:
- name: AnalysisObject
  property_count: 5
  slug: virustotal-analysis-object
- name: AttackTacticObject
  property_count: 5
  slug: virustotal-attack-tactic-object
- name: AttackTechniqueObject
  property_count: 5
  slug: virustotal-attack-technique-object
- name: CollectionObject
  property_count: 5
  slug: virustotal-collection-object
- name: CommentObject
  property_count: 5
  slug: virustotal-comment-object
- name: DomainObject
  property_count: 5
  slug: virustotal-domain-object
- name: FileBehaviourObject
  property_count: 5
  slug: virustotal-file-behaviour-object
- name: FileObject
  property_count: 5
  slug: virustotal-file-object
- name: GraphObject
  property_count: 5
  slug: virustotal-graph-object
- name: GroupObject
  property_count: 5
  slug: virustotal-group-object
- name: IocStreamNotificationObject
  property_count: 5
  slug: virustotal-ioc-stream-notification-object
- name: IpAddressObject
  property_count: 5
  slug: virustotal-ip-address-object
- name: LivehuntRulesetObject
  property_count: 5
  slug: virustotal-livehunt-ruleset-object
- name: PopularThreatCategoryObject
  property_count: 5
  slug: virustotal-popular-threat-category-object
- name: RetrohuntJobObject
  property_count: 5
  slug: virustotal-retrohunt-job-object
- name: UrlObject
  property_count: 5
  slug: virustotal-url-object
- name: UserObject
  property_count: 5
  slug: virustotal-user-object
- name: VoteObject
  property_count: 5
  slug: virustotal-vote-object
- name: YaraRuleObject
  property_count: 5
  slug: virustotal-yara-rule-object
json_structures:
- name: Virustotal Analysis Object Structure
  property_count: 5
  slug: virustotal-analysis-object-structure
- name: Virustotal Attack Tactic Object Structure
  property_count: 5
  slug: virustotal-attack-tactic-object-structure
- name: Virustotal Attack Technique Object Structure
  property_count: 5
  slug: virustotal-attack-technique-object-structure
- name: Virustotal Collection Object Structure
  property_count: 5
  slug: virustotal-collection-object-structure
- name: Virustotal Comment Object Structure
  property_count: 5
  slug: virustotal-comment-object-structure
- name: Virustotal Domain Object Structure
  property_count: 5
  slug: virustotal-domain-object-structure
- name: Virustotal File Behaviour Object Structure
  property_count: 5
  slug: virustotal-file-behaviour-object-structure
- name: Virustotal File Object Structure
  property_count: 5
  slug: virustotal-file-object-structure
- name: Virustotal Graph Object Structure
  property_count: 5
  slug: virustotal-graph-object-structure
- name: Virustotal Group Object Structure
  property_count: 5
  slug: virustotal-group-object-structure
- name: Virustotal Ioc Stream Notification Object Structure
  property_count: 5
  slug: virustotal-ioc-stream-notification-object-structure
- name: Virustotal Ip Address Object Structure
  property_count: 5
  slug: virustotal-ip-address-object-structure
- name: Virustotal Livehunt Ruleset Object Structure
  property_count: 5
  slug: virustotal-livehunt-ruleset-object-structure
- name: Virustotal Popular Threat Category Object Structure
  property_count: 5
  slug: virustotal-popular-threat-category-object-structure
- name: Virustotal Retrohunt Job Object Structure
  property_count: 5
  slug: virustotal-retrohunt-job-object-structure
- name: Virustotal Url Object Structure
  property_count: 5
  slug: virustotal-url-object-structure
- name: Virustotal User Object Structure
  property_count: 5
  slug: virustotal-user-object-structure
- name: Virustotal Vote Object Structure
  property_count: 5
  slug: virustotal-vote-object-structure
- name: Virustotal Yara Rule Object Structure
  property_count: 5
  slug: virustotal-yara-rule-object-structure
jsonld:
- class_count: 30
  name: Virustotal Context
  property_count: 156
  slug: virustotal-context
layout: provider
modified: '2026-05-29'
name: VirusTotal
nav: Providers
network: true
overview: 'VirusTotal publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Access Control - Group Management API, Access Control - Quota Management API, Access Control - Service Account Management API, and 30 more. Tagged areas include Anti Malware, Threat Intelligence, Security, File Analysis, and URL Analysis.


  The VirusTotal catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  VirusTotal''s developer surface includes authentication, documentation, API reference, engineering blog, CLI, tooling, and 31 more developer resources.'
plans:
- name: Virustotal Plans Pricing
  plan_count: 3
  slug: virustotal-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 10
  name: Virustotal Rate Limits
  slug: virustotal-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: VirusTotal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: virustotal-jsonschema-spectral-rules
- effective_rule_count: 81
  extends:
  - spectral:oas
  name: VirusTotal API Rules
  rule_count: 40
  severity_counts:
    error: 15
    hint: 0
    info: 6
    warn: 19
  slug: virustotal-rules
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 84.5
    catalog_earned_first_party: 0.0
    catalog_gap: 30.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 68.9
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virustotal/refs/heads/main/screenshots/virustotal-2026-06-20T201042.png
security:
- kind: authentication
  name: Virustotal Authentication
  slug: virustotal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Virustotal Domain Security
  slug: virustotal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: virustotal
tags:
- Anti Malware
- Threat Intelligence
- Security
- File Analysis
- URL Analysis
- YARA
- IOC
- Sandbox
- MITRE ATT&CK
- Google Cloud
website: https://www.virustotal.com
---
