---
aid: palo-alto-networks
url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/apis.yml
apis:
- aid: palo-alto-networks:pan-os-rest-api
  name: PAN-OS REST API
  tags:
  - Configuration
  - Firewall
  - Network Security
  - Policies
  - REST API
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{firewall}/restapi/v10.2
  humanURL: https://pan.dev/panos/docs/restapi/
  properties:
  - url: https://pan.dev/panos/docs/restapi/
    type: Documentation
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/get-started-with-the-pan-os-rest-api
    type: GettingStarted
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/pan-os-rest-api-reference
    type: APIReference
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/get-started-with-the-pan-os-rest-api/get-your-api-key
    type: Authentication
  - url: openapi/palo-alto-pan-os-rest-api-openapi-original.yml
    type: OpenAPI
  description: A RESTful API for managing PAN-OS next-generation firewalls including security policies, network objects, address groups, and device configuration. The REST API provides simplified JSON-based access to common firewall operations as an alternative to the XML API. Supports CRUD operations on policy rules, address objects, service objects, and security profiles. Authentication uses API keys generated from the firewall management interface or via the XML API keygen command.
- aid: palo-alto-networks:pan-os-xml-api
  name: PAN-OS XML API
  tags:
  - Configuration
  - Firewall
  - Monitoring
  - Operations
  - XML
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{firewall}/api/
  humanURL: https://pan.dev/panos/docs/xmlapi/
  properties:
  - url: https://pan.dev/panos/docs/xmlapi/
    type: Documentation
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/get-started-with-the-pan-os-xml-api
    type: GettingStarted
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/pan-os-xml-api-request-types
    type: APIReference
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/get-started-with-the-pan-os-xml-api/get-your-api-key
    type: Authentication
  - url: json-schema/pan-os-security-rule-schema.json
    type: JSONSchema
  description: The comprehensive XML-based API for PAN-OS providing full access to all firewall configuration, operational commands, reporting, logging, and commit operations. Supports request types including keygen for authentication, config for configuration changes using XPath, op for operational commands, report for generating reports, log for retrieving traffic and threat logs, and user-id for dynamic user-to-IP mapping.
- aid: palo-alto-networks:openconfig-api
  name: PAN-OS OpenConfig API
  tags:
  - Firewall
  - gNMI
  - Network Automation
  - OpenConfig
  - Telemetry
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{firewall}
  humanURL: https://docs.paloaltonetworks.com/openconfig
  properties:
  - url: https://docs.paloaltonetworks.com/openconfig
    type: Documentation
  - url: https://docs.paloaltonetworks.com/openconfig/2-0/openconfig-admin/getting-started
    type: GettingStarted
  - url: https://docs.paloaltonetworks.com/openconfig/2-0/openconfig-admin/pan-os-models/pan-os-openconfig-xmlapi
    type: APIReference
  description: Management interface for PAN-OS based on OpenConfig standard data models, providing gNMI and gNOI services through the OpenConfig plugin. Supports network automation for BGP, interfaces, LACP, LLDP, VLANs, local routes, system, and platform configuration, as well as telemetry streaming. Includes a PAN-OS OpenConfig XML API for integration with standard network management tools.
- aid: palo-alto-networks:panorama-api
  name: Panorama API
  tags:
  - Centralized Management
  - Device Groups
  - Firewall
  - Orchestration
  - Templates
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{panorama}/api/
  humanURL: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/panorama-api
  properties:
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api/panorama-api
    type: Documentation
  - url: https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-panorama-api
    type: APIReference
  description: The Panorama API uses the same PAN-OS XML and REST API interfaces but provides centralized management of multiple firewalls from a single management server. Supports device group and template stack operations for pushing configuration to managed firewalls, centralized logging and reporting, and multi-device commit workflows. Panorama-specific API operations include managing device groups, template stacks, log collectors, and performing push operations to managed devices.
- aid: palo-alto-networks:strata-cloud-manager-api
  name: Strata Cloud Manager API
  tags:
  - Cloud Management
  - Configuration
  - NGFW
  - SASE
  - Unified Management
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.strata.paloaltonetworks.com
  humanURL: https://pan.dev/scm/docs/home/
  properties:
  - url: https://pan.dev/scm/docs/home/
    type: Documentation
  - url: https://pan.dev/scm/api/
    type: APIReference
  - url: https://pan.dev/scm/docs/getstarted/
    type: GettingStarted
  - url: https://pan.dev/scm/docs/api-call/
    type: GettingStarted
  - url: https://pan.dev/scm/docs/api-best-practices/
    type: BestPractices
  - url: https://pan.dev/scm/docs/release-notes/
    type: ChangeLog
  - url: openapi/palo-alto-strata-cloud-manager-api-openapi-original.yml
    type: OpenAPI
  description: A unified cloud-based API for managing Palo Alto Networks next-generation firewalls and SASE from a single management plane. Strata Cloud Manager provides configuration management for security policies, network objects, and device settings across hardware, virtual, and cloud-native firewalls. The API uses OAuth 2.0 authentication with bearer tokens and provides RESTful endpoints for policy lifecycle management, object CRUD operations, and deployment workflows.
- aid: palo-alto-networks:cloud-ngfw-api
  name: Cloud NGFW API
  tags:
  - AWS
  - Azure
  - Cloud Security
  - Cloud-Native Firewall
  - Managed Service
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.{region}.aws.cloudngfw.paloaltonetworks.com
  humanURL: https://pan.dev/cloudngfw/aws/api/
  properties:
  - url: https://pan.dev/cloudngfw/aws/api/
    type: Documentation
  - url: https://pan.dev/cloudngfw/docs/getstarted_azure/
    type: GettingStarted
  - url: openapi/palo-alto-cloud-ngfw-api-openapi-original.yml
    type: OpenAPI
  description: REST APIs for managing Palo Alto Networks Cloud NGFW, a cloud-native managed firewall service available on AWS and Azure. The API supports creating and managing firewall resources, configuring security rules and rule stacks, managing FQDN lists and prefix lists, and retrieving firewall logs. On AWS, authentication uses IAM roles; on Azure, authentication uses Azure Active Directory.
- aid: palo-alto-networks:wildfire-api
  name: WildFire API
  tags:
  - File Analysis
  - Malware Analysis
  - Sandbox
  - Threat Prevention
  - Verdicts
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://wildfire.paloaltonetworks.com/publicapi/
  humanURL: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api
  properties:
  - url: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api
    type: Documentation
  - url: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api/get-started-with-the-wildfire-api
    type: GettingStarted
  - url: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api
    type: APIReference
  - url: openapi/palo-alto-wildfire-api-openapi-original.yml
    type: OpenAPI
  description: A cloud-based API for submitting files, URLs, and links for advanced malware analysis in the WildFire sandbox environment. The API returns threat verdicts (benign, malware, grayware, phishing) and detailed analysis reports including behavioral indicators, network activity, and file artifacts. Supports file submission via multipart form upload, verdict queries by hash (MD5, SHA-256), and retrieval of PCAP files and detailed analysis reports.
- aid: palo-alto-networks:threat-vault-api
  name: Threat Vault API
  tags:
  - Antivirus
  - CVE
  - IPS
  - Signatures
  - Threat Intelligence
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.threatvault.paloaltonetworks.com
  humanURL: https://pan.dev/threat-vault/api/
  properties:
  - url: https://pan.dev/threat-vault/api/
    type: Documentation
  - url: https://pan.dev/cdss/docs/getstarted/
    type: GettingStarted
  - url: https://pan.dev/cdss/docs/authentication/
    type: Authentication
  - url: https://pan.dev/cdss/docs/api-call/
    type: GettingStarted
  - url: openapi/palo-alto-threat-vault-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for querying Palo Alto Networks threat signature metadata, content release notes, and threat intelligence data. The API provides access to antivirus signatures, anti-spyware signatures, vulnerability protection (IPS) signatures, and file type identification data. Supports queries by signature ID, CVE, threat name, and content release version. Replaces the deprecated AutoFocus API for threat intelligence lookups. Requires an Advanced Threat Prevention or Threat Prevention subscription.
- aid: palo-alto-networks:autofocus-api
  name: AutoFocus API (Deprecated)
  tags:
  - Analysis
  - Deprecated
  - Malware
  - Threat Intelligence
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://autofocus.paloaltonetworks.com/api/v1.0/
  humanURL: https://docs.paloaltonetworks.com/autofocus/autofocus-api
  properties:
  - url: https://docs.paloaltonetworks.com/autofocus/autofocus-api
    type: Documentation
  - url: https://docs.paloaltonetworks.com/autofocus/autofocus-api/get-started-with-the-autofocus-api
    type: GettingStarted
  description: A threat intelligence API that provided contextual information about malware, campaigns, and threat actors observed across the Palo Alto Networks global threat intelligence network. AutoFocus reached end-of-sale on September 30, 2022, and end-of-support on September 30, 2025. Developers should migrate to the Threat Vault API for threat signature lookups and to Cortex XDR or XSIAM for advanced threat intelligence and investigation capabilities.
- aid: palo-alto-networks:iot-security-api
  name: IoT Security API
  tags:
  - Asset Discovery
  - Device Security
  - IoT
  - Network Segmentation
  - OT Security
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{customer}.iot.paloaltonetworks.com/pub/v4.0/
  humanURL: https://pan.dev/iot/api/
  properties:
  - url: https://pan.dev/iot/api/
    type: Documentation
  - url: openapi/palo-alto-iot-security-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for managing IoT and OT device security including device discovery, profiling, vulnerability assessment, and security policy recommendations. The API provides endpoints for retrieving discovered device inventories, security alerts, vulnerability details, and recommended network segmentation policies. Authentication uses X-Key-Id and X-Access-Key headers with keys generated from the IoT Security portal. Rate limited to 60 requests per minute.
- aid: palo-alto-networks:dlp-api
  name: Data Loss Prevention API
  tags:
  - Compliance
  - Data Classification
  - Data Security
  - DLP
  - Incident Management
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://pan.dev/dlp/api/
  properties:
  - url: https://pan.dev/dlp/api/
    type: Documentation
  - url: openapi/palo-alto-dlp-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for managing enterprise data loss prevention across Palo Alto Networks platforms. The API provides access to DLP incidents, policy violation reports, data pattern matches, and remediation workflows. Supports reviewing and managing incidents detected across network traffic, cloud applications, and email channels. Uses SASE OAuth 2.0 authentication aligned with the broader Prisma SASE authentication framework.
- aid: palo-alto-networks:prisma-access-api
  name: Prisma Access API
  tags:
  - Cloud Security
  - Configuration
  - Remote Access
  - SASE
  - Zero Trust
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/access/api/prisma-access-config/
  properties:
  - url: https://pan.dev/access/api/prisma-access-config/
    type: Documentation
  - url: https://pan.dev/access/api/insights/
    type: APIReference
  - url: https://pan.dev/sase/docs/
    type: GettingStarted
  - url: https://pan.dev/sase/docs/release-notes/changelog/
    type: ChangeLog
  - url: openapi/palo-alto-prisma-access-api-openapi-original.yml
    type: OpenAPI
  description: REST APIs for configuring and monitoring Prisma Access, Palo Alto Networks' cloud-delivered SASE platform. The Configuration API manages security policies, remote networks, service connections, and mobile user configurations for cloud-managed tenants. The Insights API (versions 1.0 through 3.0) provides health monitoring, tunnel status, bandwidth utilization, and user connectivity data.
- aid: palo-alto-networks:autonomous-dem-api
  name: Autonomous DEM API
  tags:
  - Digital Experience
  - Monitoring
  - Network Analytics
  - Performance
  - SASE
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://pan.dev/access/api/adem/autonomous-dem-api/
  properties:
  - url: https://pan.dev/access/api/adem/autonomous-dem-api/
    type: Documentation
  - url: https://pan.dev/access/docs/adem/getstarted/
    type: GettingStarted
  - url: openapi/palo-alto-autonomous-dem-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for monitoring digital experience metrics within Prisma Access environments. The Autonomous Digital Experience Management (ADEM) API provides application performance data, network path analysis, endpoint health metrics, and user experience scoring. Supports querying performance data by user, application, location, and time range to identify connectivity and performance issues affecting remote and branch users connected through Prisma Access.
- aid: palo-alto-networks:prisma-sd-wan-api
  name: Prisma SD-WAN API
  tags:
  - Branch Networking
  - CloudGenix
  - Routing
  - SD-WAN
  - WAN Optimization
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sdwan/docs/
  properties:
  - url: https://pan.dev/sdwan/docs/
    type: Documentation
  - url: https://pan.dev/sdwan/api/
    type: APIReference
  - url: openapi/palo-alto-prisma-sd-wan-api-openapi-original.yml
    type: OpenAPI
  description: REST APIs for managing Prisma SD-WAN (formerly CloudGenix) branch networking infrastructure. The API supports configuration of sites, WAN interfaces, routing policies, application definitions, path quality monitoring, and network analytics. Provides both a unified API using SASE OAuth 2.0 authentication and a legacy API with session token authentication.
- aid: palo-alto-networks:prisma-cloud-cspm-api
  name: Prisma Cloud CSPM API
  tags:
  - Cloud Posture
  - Cloud Security
  - Compliance
  - CSPM
  - Multi-Cloud
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.prismacloud.io
  humanURL: https://pan.dev/prisma-cloud/api/cspm/
  properties:
  - url: https://pan.dev/prisma-cloud/api/cspm/
    type: Documentation
  - url: https://prisma.pan.dev/api/cloud/api-auth/
    type: Authentication
  - url: https://pan.dev/prisma-cloud/docs/cspm/cspm-gs/
    type: GettingStarted
  - url: openapi/palo-alto-prisma-cloud-cspm-api-openapi-original.yml
    type: OpenAPI
  - url: asyncapi/palo-alto-prisma-cloud-webhooks-asyncapi-original.yml
    type: AsyncAPI
  - url: json-schema/prisma-cloud-policy-schema.json
    type: JSONSchema
  description: The Cloud Security Posture Management API for Prisma Cloud (formerly RedLock) providing programmatic access to cloud security monitoring across AWS, Azure, GCP, and Oracle Cloud. The API supports managing security alerts, compliance policies, cloud accounts, asset inventories, and remediation workflows. Endpoints cover alert management, policy configuration, compliance reporting, cloud account onboarding, resource queries using RQL (Resource Query Language), and integration management.
- aid: palo-alto-networks:prisma-cloud-compute-api
  name: Prisma Cloud Compute API
  tags:
  - Container Security
  - CWPP
  - Kubernetes
  - Runtime Protection
  - Serverless
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{console}/api/v1
  humanURL: https://pan.dev/compute/api/
  properties:
  - url: https://pan.dev/compute/api/
    type: Documentation
  - url: https://pan.dev/compute/api/access-api-self-hosted/
    type: Authentication
  - url: https://pan.dev/compute/api/stable-endpoints/
    type: APIReference
  - url: openapi/palo-alto-prisma-cloud-compute-api-openapi-original.yml
    type: OpenAPI
  description: The Cloud Workload Protection Platform (CWPP) API for Prisma Cloud (formerly Twistlock) providing security for containers, hosts, and serverless functions. The API covers image vulnerability scanning, runtime defense policies, compliance checks, registry scanning, CI/CD pipeline integration, and defender deployment management. Supports both SaaS and self-hosted Console deployments.
- aid: palo-alto-networks:prisma-cloud-code-security-api
  name: Prisma Cloud Code Security API
  tags:
  - Code Security
  - DevSecOps
  - IaC Scanning
  - Shift Left
  - Supply Chain
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.prismacloud.io
  humanURL: https://pan.dev/prisma-cloud/api/code/
  properties:
  - url: https://pan.dev/prisma-cloud/api/code/
    type: Documentation
  - url: openapi/palo-alto-prisma-cloud-code-security-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for Prisma Cloud Application Security (formerly Bridgecrew) providing infrastructure-as-code scanning, software composition analysis, and supply chain security. The API supports checking Terraform, CloudFormation, Kubernetes manifests, and Dockerfiles against security policies, managing code repositories, retrieving scan results, and configuring fix suggestions. Integrates with CI/CD pipelines for shift-left security enforcement during the development lifecycle.
- aid: palo-alto-networks:cortex-xdr-api
  name: Cortex XDR API
  tags:
  - Detection
  - Endpoint Security
  - Incidents
  - Response
  - XDR
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api-{fqdn}/public_api/v1/
  humanURL: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API
  properties:
  - url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API
    type: Documentation
  - url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-APIs
    type: GettingStarted
  - url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/API-Reference
    type: APIReference
  - url: openapi/palo-alto-cortex-xdr-api-openapi-original.yml
    type: OpenAPI
  - url: asyncapi/palo-alto-cortex-xdr-webhooks-asyncapi-original.yml
    type: AsyncAPI
  - url: json-schema/cortex-xdr-incident-schema.json
    type: JSONSchema
  description: A REST API for the Cortex XDR extended detection and response platform providing programmatic access to incident management, alert handling, endpoint operations, and threat hunting. Key API modules include incidents (get, update, close), alerts (get details, exclusions), endpoints (isolate, unisolate, scan, get agent info), scripts (execute, get results), and audit logs.
- aid: palo-alto-networks:cortex-xsoar-api
  name: Cortex XSOAR API
  tags:
  - Automation
  - Incident Response
  - Integrations
  - Playbooks
  - SOAR
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{xsoar-server}/
  humanURL: https://xsoar.pan.dev/
  properties:
  - url: https://xsoar.pan.dev/
    type: Documentation
  - url: https://xsoar.pan.dev/docs/reference/api/demisto-class
    type: APIReference
  - url: https://xsoar.pan.dev/docs/concepts/getting-started-guide
    type: GettingStarted
  - url: https://xsoar.pan.dev/docs/reference/index
    type: APIReference
  - url: https://cortex.marketplace.pan.dev/marketplace/
    type: Marketplace
  - url: https://github.com/demisto/content
    type: GitHubRepository
  - url: json-schema/cortex-xsoar-integration-manifest-schema.json
    type: JSONSchema
  - url: openapi/palo-alto-cortex-xsoar-api-openapi-original.yml
    type: OpenAPI
  description: APIs and development framework for Cortex XSOAR (formerly Demisto), the security orchestration, automation, and response platform. The REST API provides programmatic access to incidents, investigations, war rooms, playbooks, and integration instances. The integration development framework enables building custom integrations for the XSOAR marketplace with 750+ verified integrations. Supports Python and PowerShell integration development with the demisto-sdk CLI tool.
- aid: palo-alto-networks:cortex-xsiam-api
  name: Cortex XSIAM API
  tags:
  - AI-Driven SOC
  - Automation
  - Security Analytics
  - SIEM
  - XDR
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api-{fqdn}/public_api/v1/
  humanURL: https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM-REST-API
  properties:
  - url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM-REST-API
    type: Documentation
  - url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-APIs
    type: GettingStarted
  - url: openapi/palo-alto-cortex-xsiam-api-openapi-original.yml
    type: OpenAPI
  - url: asyncapi/palo-alto-cortex-xsiam-data-ingestion-asyncapi-original.yml
    type: AsyncAPI
  description: A REST API for Cortex XSIAM, the AI-driven security operations platform that combines SIEM, XDR, SOAR, and ASM capabilities. The API provides endpoints for incident management, alert handling, data ingestion configuration, XQL query execution, asset management, and automation rule management. Shares endpoint patterns with Cortex XDR but includes additional capabilities for log collection configuration, data model management, and AI-assisted investigation.
- aid: palo-alto-networks:prisma-airs-api
  name: Prisma AIRS API
  tags:
  - AI Runtime
  - AI Security
  - GenAI
  - LLM Security
  - Prompt Injection
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://pan.dev/airs/
  properties:
  - url: https://pan.dev/airs/
    type: Documentation
  - url: https://pan.dev/prisma-airs/api/airuntimesecurity/airuntimesecurityapi/
    type: APIReference
  - url: https://pan.dev/prisma-airs/api/airuntimesecurity/pythonsdk/
    type: SDK
  - url: https://github.com/PaloAltoNetworks/aisecurity-python-sdk
    type: GitHubRepository
  - url: openapi/palo-alto-prisma-airs-api-openapi-original.yml
    type: OpenAPI
  description: The AI Runtime Security API for securing generative AI applications against prompt injection, data leakage, toxic content, and other AI-specific threats. The API scans prompts and model responses in real time, providing threat detection and content classification for LLM-powered applications. Supports integration via REST API or the pan-aisecurity Python SDK.
- aid: palo-alto-networks:security-advisory-api
  name: Security Advisory API
  tags:
  - CVE
  - Patching
  - PSIRT
  - Security Advisories
  - Vulnerabilities
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://security.paloaltonetworks.com
  humanURL: https://security.paloaltonetworks.com/api
  properties:
  - url: https://security.paloaltonetworks.com/api
    type: Documentation
  - url: https://security.paloaltonetworks.com/rss.xml
    type: Feed
  - url: openapi/palo-alto-security-advisory-api-openapi-original.yml
    type: OpenAPI
  - url: json-schema/palo-alto-security-advisory-schema.json
    type: JSONSchema
  description: A REST API (currently in beta) for programmatically querying Palo Alto Networks security advisories published by the Product Security Incident Response Team (PSIRT). The API supports filtering advisories by CVE ID, severity, product, and date range. Returns advisory details including vulnerability descriptions, affected versions, CVSS scores, and remediation guidance. Also available as an RSS feed for continuous monitoring of new security advisories.
- aid: palo-alto-networks:cortex-xpanse-api
  name: Cortex Xpanse API
  tags:
  - Asset Discovery
  - Attack Surface Management
  - Exposure Management
  - Internet-Facing Assets
  - Risk Assessment
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api-{fqdn}/public_api/v1/
  humanURL: https://docs-cortex.paloaltonetworks.com/r/Cortex-Xpanse-REST-API
  properties:
  - url: https://docs-cortex.paloaltonetworks.com/r/Cortex-Xpanse-REST-API
    type: Documentation
  - url: openapi/palo-alto-cortex-xpanse-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for Cortex Xpanse, the attack surface management platform that discovers, evaluates, and mitigates risks on internet-facing assets. The API provides programmatic access to asset inventories, attack surface rules, risk identification, and remediation workflows. Supports querying discovered services, certificates, domains, and cloud resources exposed to the internet. Authentication uses RBAC API key pairs consistent with other Cortex platform APIs.
- aid: palo-alto-networks:dns-security-api
  name: DNS Security API
  tags:
  - Beta
  - DNS
  - Domain Categorization
  - Domain Security
  - Threat Intelligence
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.dns.service.paloaltonetworks.com
  humanURL: https://pan.dev/dns-security/api/
  properties:
  - url: https://pan.dev/dns-security/api/
    type: Documentation
  - url: https://pan.dev/cdss/docs/getstarted/
    type: GettingStarted
  - url: https://pan.dev/cdss/docs/authentication/
    type: Authentication
  - url: openapi/palo-alto-dns-security-api-openapi-original.yml
    type: OpenAPI
  description: A REST API (currently in beta) for retrieving DNS domain details, categorization information, and contextual network access statistics from the Palo Alto Networks DNS Security service. Supports querying domain reputation, categorization data, and related threat intelligence. Requires a DNS Security subscription and uses API key authentication via the X-DNS-API-APIKEY header.
- aid: palo-alto-networks:email-dlp-api
  name: Email DLP API
  tags:
  - Compliance
  - Data Protection
  - DLP
  - Email Security
  - Incident Management
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://pan.dev/email-dlp/api/
  properties:
  - url: https://pan.dev/email-dlp/api/
    type: Documentation
  - url: openapi/palo-alto-email-dlp-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for programmatically reviewing and managing Email DLP incidents detected across enterprise email channels. The API supports retrieving incident details, updating verdicts on flagged emails, and managing remediation workflows for data loss prevention violations in email traffic. Uses region-specific endpoints and requires SOC_Admin, Superuser, or Data Security Administrator roles for access.
- aid: palo-alto-networks:saas-security-api
  name: SaaS Security API
  tags:
  - CASB
  - Cloud Applications
  - Compliance
  - Data Protection
  - SaaS Security
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-api
  properties:
  - url: https://docs.paloaltonetworks.com/saas-security/saas-security-admin/saas-security-api
    type: Documentation
  - url: openapi/palo-alto-saas-security-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for scanning and protecting assets stored in sanctioned SaaS applications. The API provides at-rest detection, inspection, and remediation capabilities for data stored across cloud applications including file scanning, policy violation detection, and automated remediation workflows. Supports integration with enterprise SaaS applications for continuous data security monitoring.
- aid: palo-alto-networks:sspm-api
  name: SaaS Security Posture Management API
  tags:
  - Compliance
  - Misconfiguration
  - SaaS Applications
  - SaaS Posture
  - SSPM
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/sspm/
  properties:
  - url: https://pan.dev/sase/api/sspm/
    type: Documentation
  - url: openapi/palo-alto-sspm-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for managing SaaS Security Posture Management providing continuous monitoring of misconfigured SaaS application settings. The API supports managing onboarded SaaS applications, retrieving configuration assessment details, accessing the application catalog, and managing JIRA integrations for remediation tracking. Part of the broader SASE platform with OAuth 2.0 authentication.
- aid: palo-alto-networks:ztna-connector-api
  name: ZTNA Connector API
  tags:
  - Connectors
  - Network Access
  - SASE
  - Zero Trust
  - ZTNA
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/access/api/ztna/ztna-connector-apis/
  properties:
  - url: https://pan.dev/access/api/ztna/ztna-connector-apis/
    type: Documentation
  - url: https://pan.dev/access/api/ztna/ztna-connector-restful-api/
    type: APIReference
  - url: openapi/palo-alto-ztna-connector-api-openapi-original.yml
    type: OpenAPI
  description: REST APIs for managing Zero Trust Network Access connectors within the Prisma Access SASE platform. The API supports creating and managing ZTNA connectors, applications, licenses, and connector groups for providing secure application access without traditional VPN infrastructure. Uses the common SASE OAuth 2.0 authentication framework with tenant service group credentials.
- aid: palo-alto-networks:prisma-access-browser-api
  name: Prisma Access Browser API
  tags:
  - Browser Management
  - Enterprise Browser
  - SASE
  - Secure Browser
  - Web Security
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/access/api/browser-mgmt/browser-mgmt-api/
  properties:
  - url: https://pan.dev/access/api/browser-mgmt/browser-mgmt-api/
    type: Documentation
  - url: openapi/palo-alto-prisma-access-browser-api-openapi-original.yml
    type: OpenAPI
  description: REST APIs for scaling and automating processes related to the Prisma Access secure enterprise browser. The API supports browser deployment management, policy configuration, and user management for the cloud-delivered secure browser solution. Supports Super User (read/write) and View-Only Administrator roles for access control.
- aid: palo-alto-networks:sase-tenancy-service-api
  name: SASE Tenancy Service API
  tags:
  - Multi-Tenant
  - SASE
  - Service Provider
  - Tenant Management
  - TSG
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/tenancy/
  properties:
  - url: https://pan.dev/sase/api/tenancy/
    type: Documentation
  - url: openapi/palo-alto-sase-tenancy-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for creating and managing Tenant Service Groups (TSGs) within the Palo Alto Networks SASE platform. The API supports building tenant hierarchies for multi-tenant deployments, managing TSG properties, and organizing service subscriptions across organizational units. Essential for managed security service providers and large enterprises with complex organizational structures. Uses OAuth 2.0 authentication.
- aid: palo-alto-networks:sase-iam-api
  name: SASE IAM API
  tags:
  - Access Control
  - Identity Management
  - RBAC
  - SASE
  - Service Accounts
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/iam/
  properties:
  - url: https://pan.dev/sase/api/iam/
    type: Documentation
  - url: openapi/palo-alto-sase-iam-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for managing identity and access on the SASE platform including creating service accounts, managing access policies, and configuring role-based access control for SASE API consumers. The API supports provisioning service account credentials used for OAuth 2.0 authentication across all SASE platform APIs. Part of the common SASE management services layer.
- aid: palo-alto-networks:sase-subscription-api
  name: SASE Subscription Service API
  tags:
  - Entitlements
  - Licensing
  - SASE
  - Subscriptions
  - Tenant Management
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/subscription/
  properties:
  - url: https://pan.dev/sase/api/subscription/
    type: Documentation
  - url: openapi/palo-alto-sase-subscription-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for managing license subscriptions assigned to Tenant Service Groups within the SASE platform. The API supports querying subscription entitlements, managing license allocations across tenant hierarchies, and retrieving subscription status information. Uses OAuth 2.0 authentication consistent with other SASE platform APIs.
- aid: palo-alto-networks:sase-aggregate-monitoring-api
  name: SASE Aggregate Monitoring API
  tags:
  - Analytics
  - Monitoring
  - Multi-Tenant
  - SASE
  - Threat Monitoring
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/mt-monitor/
  properties:
  - url: https://pan.dev/sase/api/mt-monitor/
    type: Documentation
  - url: openapi/palo-alto-sase-aggregate-monitoring-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for performing aggregated monitoring queries across SASE tenants. The API supports querying application usage, threat data, URL categorization, and license utilization across all tenants in a hierarchy. Provides multi-tenant visibility for managed security service providers and enterprise administrators overseeing multiple organizational units.
- aid: palo-alto-networks:aiops-ngfw-bpa-api
  name: AIOps for NGFW BPA API
  tags:
  - AIOps
  - Assessment
  - Best Practices
  - Configuration Analysis
  - NGFW
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://pan.dev/aiops-ngfw-bpa/api/
  properties:
  - url: https://pan.dev/aiops-ngfw-bpa/api/
    type: Documentation
  - url: openapi/palo-alto-aiops-ngfw-bpa-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for the AIOps Best Practice Assessment service that programmatically generates firewall configuration assessments against Palo Alto Networks best practice recommendations. The API supports generating BPA data, checking report status, and retrieving assessment reports in JSON format. Available for both free and premium AIOps for NGFW instances. Helps identify configuration gaps and security improvement opportunities.
- aid: palo-alto-networks:strata-logging-service-api
  name: Strata Logging Service API
  tags:
  - Analytics
  - Data Lake
  - Log Forwarding
  - Logging
  - SIEM Integration
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/cdl/docs/log-forwarding/
  properties:
  - url: https://pan.dev/cdl/docs/log-forwarding/
    type: Documentation
  - url: https://pan.dev/cdl/docs/logforwarding/release-notes/relnotes/
    type: ChangeLog
  - url: openapi/palo-alto-strata-logging-service-api-openapi-original.yml
    type: OpenAPI
  - url: asyncapi/palo-alto-strata-logging-forwarding-asyncapi-original.yml
    type: AsyncAPI
  description: REST APIs for the Strata Logging Service (formerly Cortex Data Lake) providing log forwarding and query capabilities. The Log Forwarding API manages log forwarding profiles for syslog, HTTPS, and email destinations supporting CSV, LEEF, CEF, JSON, and PARQUET formats with up to 200 syslog destinations per instance. The Query Service API enables programmatic log retrieval and pagination across collected security telemetry data.
- aid: palo-alto-networks:sase-config-orchestration-api
  name: Configuration Orchestration API
  tags:
  - Remote Networks
  - SASE
  - SD-WAN Integration
  - Third-Party
  - Tunnel Configuration
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/config-orch/configuration-orchestration-api/
  properties:
  - url: https://pan.dev/sase/api/config-orch/configuration-orchestration-api/
    type: Documentation
  - url: openapi/palo-alto-sase-config-orchestration-api-openapi-original.yml
    type: OpenAPI
  description: A REST API enabling third-party SD-WAN integration with Prisma Access Remote Networks. The API supports automated tunnel configuration, branch onboarding workflows, and coordination between third-party SD-WAN solutions and the Prisma Access SASE infrastructure. Designed for technology partners integrating their SD-WAN platforms with Palo Alto Networks SASE services.
- aid: palo-alto-networks:prisma-cloud-dspm-api
  name: Prisma Cloud DSPM API
  tags:
  - Classification
  - Cloud Data
  - Data Posture
  - Data Security
  - Multi-Cloud
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.prismacloud.io
  humanURL: https://pan.dev/prisma-cloud/api/
  properties:
  - url: https://pan.dev/prisma-cloud/api/
    type: Documentation
  - url: openapi/palo-alto-prisma-cloud-dspm-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for Data Security Posture Management within Prisma Cloud providing visibility and control over sensitive data stored across multi-cloud environments. The API supports data discovery, classification, and risk assessment for cloud data stores including databases, object storage, and file systems. Authentication uses JWT tokens consistent with the broader Prisma Cloud API framework.
- aid: palo-alto-networks:sase-5g-manage-api
  name: SASE 5G Manage Services API
  tags:
  - 5G Security
  - Agentless Security
  - Mobile Network
  - Multi-Tenant
  - Telecommunications
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/manage-services-5g/
  properties:
  - url: https://pan.dev/sase/api/manage-services-5g/
    type: Documentation
  - url: openapi/palo-alto-sase-5g-api-openapi-original.yml
    type: OpenAPI
  description: REST APIs for managing scalable, multi-tenant, agentless security for 5G networks. The API supports provisioning and configuring 5G security services that integrate with 5G authentication frameworks for securing mobile network traffic. Designed for telecommunications providers and enterprises deploying private 5G networks with Palo Alto Networks SASE security services.
- aid: palo-alto-networks:prisma-airs-ai-red-teaming-api
  name: Prisma AIRS AI Red Teaming API
  tags:
  - AI Security
  - GenAI
  - LLM Security
  - Red Teaming
  - Vulnerability Assessment
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com/ai-red-teaming
  humanURL: https://pan.dev/prisma-airs-redteam/api/ai-integration/introduction/
  properties:
  - url: https://pan.dev/prisma-airs-redteam/api/ai-integration/introduction/
    type: Documentation
  - url: https://docs.paloaltonetworks.com/ai-runtime-security/ai-red-teaming/identify-ai-system-risks-with-ai-red-teaming/get-started-with-prisma-airs-ai-red-teaming
    type: GettingStarted
  - url: openapi/palo-alto-prisma-airs-ai-red-teaming-api-openapi-original.yml
    type: OpenAPI
  description: An automated red teaming API for assessing the safety and security of generative AI systems including large language models and LLM-powered applications. The API simulates real-world threats by sending crafted attack prompts including jailbreaks, prompt injection, and input manipulation to target AI systems and evaluating responses. Supports creating scan targets, executing asynchronous vulnerability scans, and retrieving detailed reports.
- aid: palo-alto-networks:identity-security-posture-management-api
  name: Identity Security Posture Management API
  tags:
  - Access Control
  - Identity Security
  - ITDR
  - MFA
  - SSPM
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/identity-sspm/
  properties:
  - url: https://pan.dev/sase/api/identity-sspm/
    type: Documentation
  description: A REST API within the SaaS Security Posture Management framework providing security-related metrics and configurations for user and service accounts across SaaS environments. The API enables security teams to monitor, analyze, and respond to identity-related risks by connecting users, permissions, activities, and security configurations.
- aid: palo-alto-networks:sase-5g-monitor-api
  name: SASE 5G Monitor Services API
  tags:
  - 5G Security
  - Monitoring
  - Multi-Tenant
  - Network Analytics
  - Telecommunications
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/monitor-services-5g/
  properties:
  - url: https://pan.dev/sase/api/monitor-services-5g/
    type: Documentation
  description: REST APIs for monitoring 5G security services within the SASE platform. Provides telemetry, analytics, and health monitoring data for 5G network security deployments. Complements the SASE 5G Manage Services API by providing visibility into security service performance, traffic patterns, and threat detection metrics across 5G network environments. Uses OAuth 2.0 authentication.
- aid: palo-alto-networks:prisma-sase-service-status-api
  name: Prisma SASE Service Status API
  tags:
  - Incidents
  - Maintenance
  - Monitoring
  - SASE
  - Status
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://sase.status.paloaltonetworks.com/api/v2
  humanURL: https://pan.dev/sase/docs/saseservicestatusapi/
  properties:
  - url: https://pan.dev/sase/docs/saseservicestatusapi/
    type: Documentation
  description: A public JSON API for monitoring Prisma SASE service health and status built on the Atlassian StatusPage platform. Provides endpoints for overall service status, individual component health, unresolved and recent incidents, and upcoming and active scheduled maintenance windows. Returns status indicators including operational, degraded performance, partial outage, and major outage. No authentication required.
- aid: palo-alto-networks:cross-platform-service-status-api
  name: Cross-Platform Service Status API
  tags:
  - Incidents
  - Maintenance
  - Monitoring
  - Platform Health
  - Status
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://status.paloaltonetworks.com/api/v2
  humanURL: https://pan.dev/cross-platform/docs/servicestatusapi/
  properties:
  - url: https://pan.dev/cross-platform/docs/servicestatusapi/
    type: Documentation
  description: A public JSON API for monitoring the status of all Palo Alto Networks cloud services and products built on the Atlassian StatusPage platform. Provides endpoints for portfolio-wide status, individual product and service component health, unresolved and recent incidents, and scheduled maintenance events. Component statuses include operational, degraded performance, partial outage, and major outage. No authentication required.
- aid: palo-alto-networks:sase-authentication-service-api
  name: SASE Authentication Service API
  tags:
  - Access Tokens
  - Authentication
  - Identity
  - OAuth 2.0
  - SASE
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://auth.apps.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/auth/
  properties:
  - url: https://pan.dev/sase/api/auth/
    type: Documentation
  - url: https://pan.dev/sase/docs/getstarted/
    type: GettingStarted
  description: The OAuth 2.0 authentication service that provides access tokens for all Prisma SASE platform APIs. Uses Client ID and Client Secret credentials to generate short-lived bearer tokens with a 15-minute lifespan. All SASE platform APIs including Prisma Access, SD-WAN, SSPM, and management services require tokens from this endpoint. Supports tenant service group (TSG) scoping for multi-tenant environments.
- aid: palo-alto-networks:expedition-api
  name: Expedition API (Deprecated)
  tags:
  - Configuration
  - Deprecated
  - Firewall
  - Migration
  - Policy Optimization
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://{expedition-vm-ip}/api/v1/
  humanURL: https://pan.dev/expedition/docs/expedition_apiint/
  properties:
  - url: https://pan.dev/expedition/docs/expedition_apiint/
    type: Documentation
  - url: https://pan.dev/expedition/docs/expedition_workflow/
    type: GettingStarted
  description: A RESTful API for the Expedition 2.0 migration tool enabling programmatic firewall configuration migration from third-party vendors, policy optimization, and rule analysis. Supported migration from Check Point, Cisco ASA, Fortinet, and other firewall platforms to PAN-OS. Built on the Laravel PHP framework. Expedition reached end-of-support in January 2025. Developers should use Strata Cloud Manager migration tools for new migration workflows.
- aid: palo-alto-networks:sase-multitenant-notifications-api
  name: SASE Multitenant Notifications API
  tags:
  - Alerts
  - Multi-Tenant
  - Notifications
  - SASE
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/mt-notifications/
  properties:
  - url: https://pan.dev/sase/api/mt-notifications/
    type: Documentation
  description: A REST API for managing notifications and notification profiles across SASE multitenant environments. Supports creating and managing notification profiles, configuring webhook destinations, testing webhook connectivity, and retrieving notifications for security incidents, platform announcements, Prisma Access dataplane upgrades, and certificate expiry warnings across tenant hierarchies. Uses OAuth 2.0 authentication.
- aid: palo-alto-networks:sase-multitenant-interconnect-api
  name: SASE Multitenant Interconnect API
  tags:
  - Interconnect
  - Multi-Tenant
  - Network Routing
  - SASE
  - Service Provider
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/sase/api/mt-interconnect/multitenant-interconnect-apis/
  properties:
  - url: https://pan.dev/sase/api/mt-interconnect/multitenant-interconnect-apis/
    type: Documentation
  description: A REST API for managing service provider interconnect configurations within the SASE platform. Enables using service provider backbones for directing Prisma Access egress traffic instead of relying on public cloud providers. Supports managing traffic routing preferences on a per-service-provider and per-region basis for telecommunications partners including BT, Orange, and AT&T. Uses OAuth 2.0 authentication.
- aid: palo-alto-networks:cloud-identity-engine-api
  name: Cloud Identity Engine API
  tags:
  - Active Directory
  - Azure AD
  - Cloud Identity
  - Directory Sync
  - Identity
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.strata.paloaltonetworks.com
  humanURL: https://pan.dev/scm/api/config/ciedss/ciedss/
  properties:
  - url: https://pan.dev/scm/api/config/ciedss/ciedss/
    type: Documentation
  - url: https://pan.dev/scm/docs/getstarted/
    type: GettingStarted
  description: A REST API for the Cloud Identity Engine (CIE) Directory Sync Service that aggregates, normalizes, and provides access to enterprise identity data from multiple directory sources through a unified API. Supports synchronization of user, group, and organizational unit data from Active Directory, Azure Active Directory, Okta, Google Workspace, and PingFederate. Provides enriched user context including device, location, and logon event data for identity-aware security policies.
- aid: palo-alto-networks:prisma-cloud-mssp-api
  name: Prisma Cloud MSSP API
  tags:
  - Cloud Security
  - Licensing
  - Managed Services
  - MSSP
  - Multi-Tenant
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.prismacloud.io
  humanURL: https://pan.dev/prisma-cloud/api/mssp/prisma-cloud-managed-security-service-provider-mssp/
  properties:
  - url: https://pan.dev/prisma-cloud/api/mssp/prisma-cloud-managed-security-service-provider-mssp/
    type: Documentation
  description: A REST API enabling Managed Security Service Providers to manage multi-tenant security operations at scale within Prisma Cloud. The API provides endpoints for policy group and tenant group management, user account administration, license usage tracking, tenant lifecycle operations, stack mapping, and proxy endpoint provisioning. Authentication uses JWT-based bearer tokens supporting both service-to-service and user-to-service authentication schemes.
- aid: palo-alto-networks:vm-series-licensing-api
  name: VM-Series Licensing API
  tags:
  - Automation
  - Firewall
  - Licensing
  - Virtualization
  - VM-Series
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://licensing.paloaltonetworks.com
  humanURL: https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api
  properties:
  - url: https://docs.paloaltonetworks.com/vm-series/10-2/vm-series-deployment/license-the-vm-series-firewall/vm-series-models/licensing-api
    type: Documentation
  description: A REST API for licensing VM-Series virtual firewalls that do not have direct internet access to the Palo Alto Networks license server. Supports automated license activation, deactivation, and management for VM-Series deployments across private clouds and air-gapped environments. Enables integration with orchestration platforms for automated firewall provisioning and license lifecycle management.
- aid: palo-alto-networks:prisma-access-insights-api
  name: Prisma Access Insights API
  tags:
  - Analytics
  - Monitoring
  - Network Health
  - Prisma Access
  - SASE
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.sase.paloaltonetworks.com
  humanURL: https://pan.dev/access/api/insights/
  properties:
  - url: https://pan.dev/access/api/insights/
    type: Documentation
  - url: https://pan.dev/access/api/insights/1.0/
    type: APIReference
  - url: https://pan.dev/access/api/insights/2.0/
    type: APIReference
  - url: https://pan.dev/access/api/insights/3.0/
    type: APIReference
  - url: https://pan.dev/sase/docs/getstarted/
    type: GettingStarted
  - url: openapi/palo-alto-prisma-access-insights-api-openapi-original.yml
    type: OpenAPI
  description: A REST API for querying the health and performance of Prisma Access network deployments across multiple API versions (v1.0, v2.0, v3.0). Supports data resource queries for tunnel status, bandwidth utilization, connected user analytics, site health, accelerated application performance, and PAB events. Available for both cloud-managed (TSG-based) and Panorama-managed Prisma Access customers. Uses OAuth 2.0 bearer token authentication consistent with the SASE platform.
name: Palo Alto Networks
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Palo Alto Networks is a global cybersecurity leader providing advanced security platforms and services across network security, cloud security, and security operations. Its developer platform at pan.dev offers REST and XML APIs for PAN-OS firewalls, Strata Cloud Manager, Prisma Cloud (CSPM, CWPP, code security), Prisma Access and SD-WAN for SASE, Cortex XDR/XSOAR/XSIAM for security operations, and cloud-delivered security services including WildFire, Threat Vault, IoT Security, and DLP.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

