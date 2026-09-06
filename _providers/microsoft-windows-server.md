---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Microsoft Windows Server Agentic Access
  operation_count: 15
  slug: microsoft-windows-server-agentic-access
  summary_line: 15 operations · 9 acting
api_count: 1
apis:
- description: PowerShell and WMI-based management APIs for Windows Server administration.
  name: Windows Server Management API
  slug: windows-server-management-api
- description: WS-Management protocol implementation for remote management of Windows servers using SOAP-based web services for configuration and operations.
  name: Windows Remote Management (WinRM)
  slug: windows-remote-management-winrm
- description: LDAP and REST APIs for Active Directory management and authentication.
  name: Active Directory Domain Services API
  slug: active-directory-domain-services-api
- description: APIs for managing Hyper-V virtualization platform including virtual machines, virtual switches, and virtual storage.
  name: Hyper-V Management API
  slug: hyper-v-management-api
- description: APIs for managing Windows updates across enterprise environments.
  name: Windows Server Update Services (WSUS) API
  slug: windows-server-update-services-wsus-api
- description: Modern web-based management interface REST API for Windows Server that provides a gateway service for relaying commands and scripts to managed nodes.
  name: Windows Admin Center API
  slug: windows-admin-center-api
- description: APIs for managing Windows DNS Server services.
  name: DNS Server Management API
  slug: dns-server-management-api
- description: Infrastructure for management data and operations on Windows-based operating systems providing COM, scripting, and .NET APIs for system administration and monitoring.
  name: Windows Management Instrumentation (WMI) API
  slug: windows-management-instrumentation-wmi-api
- description: Win32 API for managing Remote Desktop Services including session management, virtual channels, user configuration, and the Remote Desktop Protocol.
  name: Remote Desktop Services API
  slug: remote-desktop-services-api
- description: APIs for defining and managing software and hardware components on failover clusters to increase application scalability and availability.
  name: Failover Clustering API
  slug: failover-clustering-api
- description: APIs and PowerShell cmdlets for managing Dynamic Host Configuration Protocol server services including leases, reservations, and scopes.
  name: DHCP Server Management API
  slug: dhcp-server-management-api
- description: Server Message Block protocol APIs and WMI management classes for managing file shares, share access, and network file sharing across Windows Server environments.
  name: SMB File Server API
  slug: smb-file-server-api
- description: API for instrumenting, querying, and consuming event logs on Windows Server for diagnostics, monitoring, and auditing.
  name: Windows Event Log API
  slug: windows-event-log-api
- description: APIs and PowerShell management for software-defined storage enabling clustering of servers with internal storage for hyper-converged infrastructure.
  name: Storage Spaces Direct API
  slug: storage-spaces-direct-api
- description: Network Policy Server providing centralized RADIUS authentication, authorization, and accounting for wireless, VPN, and dial-up connections.
  name: Network Policy Server (NPS) RADIUS API
  slug: network-policy-server-nps-radius-api
- baseURL: https://localhost
  baseurl_source: declared
  description: Application pools provide an isolation mechanism for processes on the web server. There are many different settings available to fine-tune the behavior of the worker processes used to serve requests t
  name: Microsoft Windows Server Application Pools API
  slug: microsoft-windows-server-application-pools-api
- baseURL: https://localhost
  baseurl_source: declared
  description: Applications provide a method to differentiate sections of a web site. An application belongs to a single web site and will handle requests for the web site at the application path.
  name: Microsoft Windows Server Applications API
  slug: microsoft-windows-server-applications-api
- baseURL: https://localhost
  baseurl_source: declared
  description: Web sites are a core entity of IIS that determine where and how requests will be handled. The web site API allows consumers to create, read, delete, or update their web sites.
  name: Microsoft Windows Server Web Sites API
  slug: microsoft-windows-server-web-sites-api
artifact_total: 171
collections:
- collection_type: postman
  name: IIS Administration Application Pools API
  slug: postman-microsoft-windows-server-application-pools-api
- collection_type: postman
  name: IIS Administration Application Pools Applications API
  slug: postman-microsoft-windows-server-applications-api
- collection_type: postman
  name: IIS Administration Application Pools Web Sites API
  slug: postman-microsoft-windows-server-web-sites-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IIS Administration API
  slug: open-iis-administration-api
- collection_type: open
  name: IIS Administration Application Pools API
  slug: open-microsoft-windows-server-application-pools-api
- collection_type: open
  name: IIS Administration Application Pools Applications API
  slug: open-microsoft-windows-server-applications-api
- collection_type: open
  name: IIS Administration Application Pools Web Sites API
  slug: open-microsoft-windows-server-web-sites-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Microsoft/windows-admin-center-sdk/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/microsoft/windows-admin-center-sdk/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/microsoft/.github/blob/main/CODE_OF_CONDUCT.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-windows-server/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-windows-server-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-windows-server-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-windows-server-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.microsoft.com/windows-server/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/windows-server
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/windows-server/bg-p/WindowsServer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/MicrosoftDocs/windowsserverdocs
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/windows-server/security/tls/tls-ssl-schannel-ssp-overview
created: '2024'
description: APIs and integration points for Microsoft Windows Server operating system including management, networking, storage, virtualization, security, and remote administration capabilities for enterprise server infrastructure.
examples:
- key_count: 5
  name: Iis Administration Application Create Example
  slug: iis-administration-application-create-example
- key_count: 5
  name: Iis Administration Application Example
  slug: iis-administration-application-example
- key_count: 0
  name: Iis Administration Application Links Example
  slug: iis-administration-application-links-example
- key_count: 6
  name: Iis Administration Application Pool Create Example
  slug: iis-administration-application-pool-create-example
- key_count: 8
  name: Iis Administration Application Pool Example
  slug: iis-administration-application-pool-example
- key_count: 0
  name: Iis Administration Application Pool Links Example
  slug: iis-administration-application-pool-links-example
- key_count: 3
  name: Iis Administration Application Pool Reference Example
  slug: iis-administration-application-pool-reference-example
- key_count: 4
  name: Iis Administration Application Pool Summary Example
  slug: iis-administration-application-pool-summary-example
- key_count: 6
  name: Iis Administration Application Pool Update Example
  slug: iis-administration-application-pool-update-example
- key_count: 4
  name: Iis Administration Application Summary Example
  slug: iis-administration-application-summary-example
- key_count: 4
  name: Iis Administration Application Update Example
  slug: iis-administration-application-update-example
- key_count: 6
  name: Iis Administration Binding Example
  slug: iis-administration-binding-example
- key_count: 6
  name: Iis Administration Certificate Example
  slug: iis-administration-certificate-example
- key_count: 6
  name: Iis Administration Cpu Settings Example
  slug: iis-administration-cpu-settings-example
- key_count: 3
  name: Iis Administration Error Example
  slug: iis-administration-error-example
- key_count: 1
  name: Iis Administration Hal Link Example
  slug: iis-administration-hal-link-example
- key_count: 3
  name: Iis Administration Identity Example
  slug: iis-administration-identity-example
- key_count: 5
  name: Iis Administration Periodic Restart Example
  slug: iis-administration-periodic-restart-example
- key_count: 8
  name: Iis Administration Process Model Example
  slug: iis-administration-process-model-example
- key_count: 3
  name: Iis Administration Process Orphaning Example
  slug: iis-administration-process-orphaning-example
- key_count: 6
  name: Iis Administration Rapid Fail Protection Example
  slug: iis-administration-rapid-fail-protection-example
- key_count: 2
  name: Iis Administration Recycling Example
  slug: iis-administration-recycling-example
- key_count: 8
  name: Iis Administration Recycling Log Events Example
  slug: iis-administration-recycling-log-events-example
- key_count: 6
  name: Iis Administration Web Site Create Example
  slug: iis-administration-web-site-create-example
- key_count: 8
  name: Iis Administration Web Site Example
  slug: iis-administration-web-site-example
- key_count: 4
  name: Iis Administration Web Site Limits Example
  slug: iis-administration-web-site-limits-example
- key_count: 0
  name: Iis Administration Web Site Links Example
  slug: iis-administration-web-site-links-example
- key_count: 3
  name: Iis Administration Web Site Reference Example
  slug: iis-administration-web-site-reference-example
- key_count: 4
  name: Iis Administration Web Site Summary Example
  slug: iis-administration-web-site-summary-example
- key_count: 6
  name: Iis Administration Web Site Update Example
  slug: iis-administration-web-site-update-example
features:
- description: REST API for managing IIS web sites, applications, and application pools with full CRUD operations and configuration management.
  name: Web Server Management
- description: LDAP and API-based management of directory services, user authentication, group policies, and domain controllers.
  name: Active Directory Services
- description: Create, manage, and monitor virtual machines, virtual switches, and storage with PowerShell and WMI APIs.
  name: Hyper-V Virtualization
- description: Manage servers remotely through WinRM, PowerShell Remoting, Windows Admin Center, and Remote Desktop Services.
  name: Remote Server Administration
- description: High availability clustering with automatic failover for critical workloads including SQL Server, Hyper-V, and file servers.
  name: Failover Clustering
- description: Storage Spaces Direct for hyper-converged infrastructure with pool management, tiering, and resilient storage volumes.
  name: Software-Defined Storage
- description: Network infrastructure services with APIs for DNS zone management and DHCP scope configuration.
  name: DNS and DHCP Services
- description: RADIUS authentication via NPS, TLS/SSL management, Windows Event Log auditing, and security policy enforcement.
  name: Security and Compliance
finops:
- name: Microsoft Windows Server Finops
  service_category: Operating System / Server
  slug: microsoft-windows-server-finops
image: /assets/icons/microsoft-windows-server.png
json_schemas:
- name: ApplicationCreate
  property_count: 5
  slug: iis-administration-application-create
- name: ApplicationLinks
  property_count: 0
  slug: iis-administration-application-links
- name: ApplicationPoolCreate
  property_count: 6
  slug: iis-administration-application-pool-create
- name: ApplicationPoolLinks
  property_count: 0
  slug: iis-administration-application-pool-links
- name: ApplicationPoolReference
  property_count: 3
  slug: iis-administration-application-pool-reference
- name: ApplicationPool
  property_count: 8
  slug: iis-administration-application-pool
- name: ApplicationPoolSummary
  property_count: 4
  slug: iis-administration-application-pool-summary
- name: ApplicationPoolUpdate
  property_count: 6
  slug: iis-administration-application-pool-update
- name: Application
  property_count: 5
  slug: iis-administration-application
- name: ApplicationSummary
  property_count: 4
  slug: iis-administration-application-summary
- name: ApplicationUpdate
  property_count: 4
  slug: iis-administration-application-update
- name: Binding
  property_count: 6
  slug: iis-administration-binding
- name: Certificate
  property_count: 6
  slug: iis-administration-certificate
- name: CpuSettings
  property_count: 6
  slug: iis-administration-cpu-settings
- name: Error
  property_count: 3
  slug: iis-administration-error
- name: HalLink
  property_count: 1
  slug: iis-administration-hal-link
- name: Identity
  property_count: 3
  slug: iis-administration-identity
- name: PeriodicRestart
  property_count: 5
  slug: iis-administration-periodic-restart
- name: ProcessModel
  property_count: 8
  slug: iis-administration-process-model
- name: ProcessOrphaning
  property_count: 3
  slug: iis-administration-process-orphaning
- name: RapidFailProtection
  property_count: 6
  slug: iis-administration-rapid-fail-protection
- name: RecyclingLogEvents
  property_count: 8
  slug: iis-administration-recycling-log-events
- name: Recycling
  property_count: 2
  slug: iis-administration-recycling
- name: WebSiteCreate
  property_count: 6
  slug: iis-administration-web-site-create
- name: WebSiteLimits
  property_count: 4
  slug: iis-administration-web-site-limits
- name: WebSiteLinks
  property_count: 0
  slug: iis-administration-web-site-links
- name: WebSiteReference
  property_count: 3
  slug: iis-administration-web-site-reference
- name: WebSite
  property_count: 8
  slug: iis-administration-web-site
- name: WebSiteSummary
  property_count: 4
  slug: iis-administration-web-site-summary
- name: WebSiteUpdate
  property_count: 6
  slug: iis-administration-web-site-update
- name: Application
  property_count: 8
  slug: microsoft-windows-server-application
- name: ApplicationCreate
  property_count: 5
  slug: microsoft-windows-server-applicationcreate
- name: ApplicationLinks
  property_count: 14
  slug: microsoft-windows-server-applicationlinks
- name: ApplicationPool
  property_count: 15
  slug: microsoft-windows-server-applicationpool
- name: ApplicationPoolCreate
  property_count: 12
  slug: microsoft-windows-server-applicationpoolcreate
- name: ApplicationPoolLinks
  property_count: 3
  slug: microsoft-windows-server-applicationpoollinks
- name: ApplicationPoolReference
  property_count: 3
  slug: microsoft-windows-server-applicationpoolreference
- name: ApplicationPoolSummary
  property_count: 4
  slug: microsoft-windows-server-applicationpoolsummary
- name: ApplicationPoolUpdate
  property_count: 12
  slug: microsoft-windows-server-applicationpoolupdate
- name: ApplicationSummary
  property_count: 4
  slug: microsoft-windows-server-applicationsummary
- name: ApplicationUpdate
  property_count: 4
  slug: microsoft-windows-server-applicationupdate
- name: Binding
  property_count: 7
  slug: microsoft-windows-server-binding
- name: Certificate
  property_count: 6
  slug: microsoft-windows-server-certificate
- name: CpuSettings
  property_count: 6
  slug: microsoft-windows-server-cpusettings
- name: Error
  property_count: 3
  slug: microsoft-windows-server-error
- name: HalLink
  property_count: 1
  slug: microsoft-windows-server-hallink
- name: Identity
  property_count: 3
  slug: microsoft-windows-server-identity
- name: PeriodicRestart
  property_count: 5
  slug: microsoft-windows-server-periodicrestart
- name: ProcessModel
  property_count: 8
  slug: microsoft-windows-server-processmodel
- name: ProcessOrphaning
  property_count: 3
  slug: microsoft-windows-server-processorphaning
- name: RapidFailProtection
  property_count: 6
  slug: microsoft-windows-server-rapidfailprotection
- name: Recycling
  property_count: 4
  slug: microsoft-windows-server-recycling
- name: RecyclingLogEvents
  property_count: 8
  slug: microsoft-windows-server-recyclinglogevents
- name: IIS Web Site
  property_count: 11
  slug: microsoft-windows-server-site
- name: WebSite
  property_count: 11
  slug: microsoft-windows-server-website
- name: WebSiteCreate
  property_count: 6
  slug: microsoft-windows-server-websitecreate
- name: WebSiteLimits
  property_count: 4
  slug: microsoft-windows-server-websitelimits
- name: WebSiteLinks
  property_count: 19
  slug: microsoft-windows-server-websitelinks
- name: WebSiteReference
  property_count: 3
  slug: microsoft-windows-server-websitereference
- name: WebSiteSummary
  property_count: 4
  slug: microsoft-windows-server-websitesummary
- name: WebSiteUpdate
  property_count: 7
  slug: microsoft-windows-server-websiteupdate
json_structures:
- name: Iis Administration Application Create Structure
  property_count: 5
  slug: iis-administration-application-create-structure
- name: Iis Administration Application Links Structure
  property_count: 0
  slug: iis-administration-application-links-structure
- name: Iis Administration Application Pool Create Structure
  property_count: 6
  slug: iis-administration-application-pool-create-structure
- name: Iis Administration Application Pool Links Structure
  property_count: 0
  slug: iis-administration-application-pool-links-structure
- name: Iis Administration Application Pool Reference Structure
  property_count: 3
  slug: iis-administration-application-pool-reference-structure
- name: Iis Administration Application Pool Structure
  property_count: 8
  slug: iis-administration-application-pool-structure
- name: Iis Administration Application Pool Summary Structure
  property_count: 4
  slug: iis-administration-application-pool-summary-structure
- name: Iis Administration Application Pool Update Structure
  property_count: 6
  slug: iis-administration-application-pool-update-structure
- name: Iis Administration Application Structure
  property_count: 5
  slug: iis-administration-application-structure
- name: Iis Administration Application Summary Structure
  property_count: 4
  slug: iis-administration-application-summary-structure
- name: Iis Administration Application Update Structure
  property_count: 4
  slug: iis-administration-application-update-structure
- name: Iis Administration Binding Structure
  property_count: 6
  slug: iis-administration-binding-structure
- name: Iis Administration Certificate Structure
  property_count: 6
  slug: iis-administration-certificate-structure
- name: Iis Administration Cpu Settings Structure
  property_count: 6
  slug: iis-administration-cpu-settings-structure
- name: Iis Administration Error Structure
  property_count: 3
  slug: iis-administration-error-structure
- name: Iis Administration Hal Link Structure
  property_count: 1
  slug: iis-administration-hal-link-structure
- name: Iis Administration Identity Structure
  property_count: 3
  slug: iis-administration-identity-structure
- name: Iis Administration Periodic Restart Structure
  property_count: 5
  slug: iis-administration-periodic-restart-structure
- name: Iis Administration Process Model Structure
  property_count: 8
  slug: iis-administration-process-model-structure
- name: Iis Administration Process Orphaning Structure
  property_count: 3
  slug: iis-administration-process-orphaning-structure
- name: Iis Administration Rapid Fail Protection Structure
  property_count: 6
  slug: iis-administration-rapid-fail-protection-structure
- name: Iis Administration Recycling Log Events Structure
  property_count: 8
  slug: iis-administration-recycling-log-events-structure
- name: Iis Administration Recycling Structure
  property_count: 2
  slug: iis-administration-recycling-structure
- name: Iis Administration Web Site Create Structure
  property_count: 6
  slug: iis-administration-web-site-create-structure
- name: Iis Administration Web Site Limits Structure
  property_count: 4
  slug: iis-administration-web-site-limits-structure
- name: Iis Administration Web Site Links Structure
  property_count: 0
  slug: iis-administration-web-site-links-structure
- name: Iis Administration Web Site Reference Structure
  property_count: 3
  slug: iis-administration-web-site-reference-structure
- name: Iis Administration Web Site Structure
  property_count: 8
  slug: iis-administration-web-site-structure
- name: Iis Administration Web Site Summary Structure
  property_count: 4
  slug: iis-administration-web-site-summary-structure
- name: Iis Administration Web Site Update Structure
  property_count: 6
  slug: iis-administration-web-site-update-structure
- name: Microsoft Windows Server Structure
  property_count: 0
  slug: microsoft-windows-server-structure
jsonld:
- class_count: 0
  name: Iis Administration Context
  property_count: 0
  slug: iis-administration-context
- class_count: 0
  name: Microsoft Windows Server Context
  property_count: 3
  slug: microsoft-windows-server-context
layout: provider
modified: '2026-05-19'
name: Microsoft Windows Server
nav: Providers
network: true
overview: 'Microsoft Windows Server publishes 3 APIs on the [APIs.io](https://apis.io/) network: Application Pools API, Applications API, and Web Sites API. Tagged areas include Data-Center, Enterprise, Infrastructure, Microsoft, and Operating System.


  The Microsoft Windows Server catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Windows Server''s developer surface includes authentication, developer portal, documentation, support, engineering blog, release notes, and 10 more developer resources.'
plans:
- name: Microsoft Windows Server Plans Pricing
  plan_count: 5
  slug: microsoft-windows-server-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Microsoft Windows Server Rate Limits
  slug: microsoft-windows-server-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Windows Server API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: microsoft-windows-server-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Microsoft Windows Server API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: microsoft-windows-server-spectral-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 60.5
    developer_ergonomics: 65.5
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 39.5
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-windows-server/refs/heads/main/screenshots/microsoft-windows-server-2026-06-20T185546.png
security:
- kind: authentication
  name: Microsoft Windows Server Authentication
  slug: microsoft-windows-server-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Windows Server Domain Security
  slug: microsoft-windows-server-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-windows-server
tags:
- Data-Center
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
use_cases:
- description: Deploy and manage web applications on IIS with automated site provisioning, SSL certificate management, and application pool isolation.
  name: Enterprise Web Hosting
- description: Automate server provisioning, configuration management, and patch deployment using PowerShell, WMI, and REST APIs.
  name: Infrastructure Automation
- description: Manage on-premises Windows Server infrastructure alongside Azure resources through Windows Admin Center and Azure Arc.
  name: Hybrid Cloud Management
- description: Deploy and manage Remote Desktop Services for virtual desktop and application delivery to remote workers.
  name: Virtual Desktop Infrastructure
- description: Configure failover clustering and storage replication for mission-critical applications requiring zero downtime.
  name: High Availability Deployments
website: https://portal.azure.com
---
