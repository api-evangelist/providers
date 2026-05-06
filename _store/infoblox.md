---
aid: infoblox
name: Infoblox
description: Infoblox is a networking and cybersecurity company providing DDI (DNS, DHCP, and IPAM) solutions and protective DNS-layer security services. Its product portfolio spans the Universal DDI suite for unified hybrid and multi-cloud network services, NIOS DDI for on-premises deployments, NIOS-X as a Service, Threat Defense for DNS-layer security, threat intelligence (TIDE) and research (Dossier), and NetMRI for network change and configuration management.
image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
url: https://raw.githubusercontent.com/api-evangelist/infoblox/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.20'
type: Contract
position: Consuming
access: 3rd-Party
apis:
  - name: Infoblox WAPI (Web API)
    description: RESTful API for managing Infoblox NIOS DDI (DNS, DHCP, IPAM) services, network objects, and configuration. The WAPI uses standard HTTP methods for CRUD operations and supports JSON and XML input and output formats.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://www.infoblox.com/products/ddi/
    baseURL: https://{grid-master}/wapi/v2.12
    tags:
      - DDI
      - DHCP
      - DNS
      - IPAM
      - Network Management
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/infoblox/refs/heads/main/openapi/infoblox-wapi-openapi.yml
      - type: Reference
        url: https://docs.infoblox.com/space/niosapi/
      - type: Authentication
        url: https://docs.infoblox.com/space/niosapi/22644231/WAPI+Authentication
      - type: Swagger
        url: https://{grid-master}/wapidoc/
      - type: Reference
        url: https://docs.infoblox.com/space/nios90/156664532/Using+NIOS+APIs
      - type: Change Log
        url: https://docs.infoblox.com/space/nios90/318210347/What's+New
      - type: Client Libraries
        url: https://github.com/infobloxopen/infoblox-go-client
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne API
    description: Cloud-native API for Infoblox BloxOne DDI and Threat Defense services. Provides RESTful web services for interacting with the Infoblox Cloud Service Platform (CSP) to manage and automate DDI services in the cloud.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://www.infoblox.com/products/bloxone-ddi/
    baseURL: https://csp.infoblox.com/api
    tags:
      - Cloud
      - DHCP
      - DNS
      - IPAM
      - Security
      - Threat Defense
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneDDI/
      - type: OpenAPI
        url: https://csp.infoblox.com/apidoc/
      - type: API Portal
        url: https://csp.infoblox.com/
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
      - type: Getting Started
        url: https://www.infoblox.com/developer-portal/getting-started/
      - type: Reference
        url: https://docs.infoblox.com/space/BloxOneDDI/186745633/Universal+DDI+API+Guide
      - type: Change Log
        url: https://docs.infoblox.com/space/BloxOneInfrastructure/332366018/BloxOne+Release+Notes
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne DNS Configuration API
    description: API for configuring DNS settings within the BloxOne platform. Manages DNS server configurations, views, ACLs, forwarding rules, and other DNS infrastructure settings through the Cloud Service Platform.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FDnsConfig
    baseURL: https://csp.infoblox.com/api/ddi/v1
    tags:
      - Cloud
      - Configuration
      - DNS
    properties:
      - type: Documentation
        url: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FDnsConfig
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne DNS Data API
    description: API for managing DNS data records within the BloxOne platform. Provides endpoints for creating, reading, updating, and deleting DNS resource records including A, AAAA, CNAME, MX, TXT, and other record types.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FDnsData
    baseURL: https://csp.infoblox.com/api/ddi/v1
    tags:
      - Cloud
      - DNS
      - Records
    properties:
      - type: Documentation
        url: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FDnsData
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne IPAM/DHCP API
    description: API for IP address management and DHCP protocol features within the BloxOne platform. Provides visibility and provisioning tools to manage networking spaces, monitoring and reporting of IP address infrastructures, and integration with DNS and DHCP protocols.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FIpamDhcp
    baseURL: https://csp.infoblox.com/api/ddi/v1
    tags:
      - Cloud
      - DHCP
      - IPAM
      - Network Management
    properties:
      - type: Documentation
        url: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FIpamDhcp
      - type: Reference
        url: https://docs.infoblox.com/space/BloxOneDDI/186843385
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne DDI Keys API
    description: API for managing TSIG and other keys used in DDI operations within the BloxOne platform. Handles creation and management of authentication keys used for securing DNS zone transfers and dynamic updates.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FDDIKeys
    baseURL: https://csp.infoblox.com/api/ddi/v1
    tags:
      - Authentication
      - DNS Security
      - Keys
    properties:
      - type: Documentation
        url: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FDDIKeys
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne Anycast Configuration API
    description: API for managing anycast configurations within the BloxOne platform. Enables high availability configuration of Infoblox applications running on customer premises by managing anycast addressing and routing.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://docs.infoblox.com/space/BloxOneDDI/186466502
    baseURL: https://csp.infoblox.com/api/anycast/v1
    tags:
      - Anycast
      - High Availability
      - Network Management
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneDDI/186466502
      - type: Reference
        url: https://docs.infoblox.com/space/BloxOneDDI/186745670
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne Infrastructure Management API
    description: API for managing BloxOne Cloud infrastructure components. Provides endpoints for managing on-premises hosts, service configurations, and infrastructure resources within the Infoblox Cloud Service Platform.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/
    baseURL: https://csp.infoblox.com/api/infra/v1
    tags:
      - Cloud
      - Infrastructure
      - Management
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneInfrastructure/
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne Host Activation API
    description: API for provisioning and activating on-premises hosts within the BloxOne platform. Handles the host activation workflow including zero touch provisioning and bootstrap configuration for on-prem deployments.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/
    baseURL: https://csp.infoblox.com/api/host_app/v1
    tags:
      - Host Activation
      - Infrastructure
      - Provisioning
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneInfrastructure/
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne DNS Forwarding Proxy API
    description: API for managing DNS Forwarding Proxy (DFP) configurations within BloxOne Threat Defense. Enforces DNS client-based security policies at remote sites by forwarding DNS queries through the Infoblox cloud for threat inspection and policy enforcement.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/
    baseURL: https://csp.infoblox.com/api/atcdfp/v1
    tags:
      - DNS
      - Forwarding Proxy
      - Security
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneThreatDefense/
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne Firewall API
    description: API for managing BloxOne Threat Defense Cloud firewall policies and security lists. Provides visibility into infected and compromised devices on the network and allows management of security policies, custom lists, and named lists for DNS-based threat defense.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/
    baseURL: https://csp.infoblox.com/api/atcfw/v1
    tags:
      - Firewall
      - Security
      - Threat Defense
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneThreatDefense/
      - type: Reference
        url: https://docs.infoblox.com/space/BloxOneThreatDefense/35406336
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne Redirect API
    description: API for configuring BloxOne Threat Defense Cloud redirect behavior. Allows configuring traffic redirection to the Infoblox server or custom destinations when threats are detected, and manages redirect pages and custom URL filtering rules.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/docs/Redirect
    baseURL: https://csp.infoblox.com/api/atcfw/v1
    tags:
      - Redirect
      - Security
      - Threat Defense
    properties:
      - type: Documentation
        url: https://csp.infoblox.com/apidoc/docs/Redirect
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox BloxOne Upgrade Policy API
    description: API for managing software upgrade policies for BloxOne on-premises hosts. Allows scheduling and configuring software and configuration updates for deployed BloxOne infrastructure components.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://csp.infoblox.com/apidoc/
    baseURL: https://csp.infoblox.com/api/upgrade_policy/v1
    tags:
      - Infrastructure
      - Policy
      - Upgrade
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneInfrastructure/
      - type: Authentication
        url: https://docs.infoblox.com/space/BloxOneDDI/35430405/Authentication
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox Threat Defense API
    description: API for threat intelligence, security analytics, and DNS firewall capabilities. Provides programmatic access to BloxOne Threat Defense features including security policy management, threat feeds, and DNS-layer security controls.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://www.infoblox.com/products/threat-defense/
    baseURL: https://csp.infoblox.com/tide/api
    tags:
      - DNS Security
      - Firewall
      - Security
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/BloxOneThreatDefense/
      - type: API Reference
        url: https://docs.infoblox.com/space/BloxOneThreatDefense/35389219/Threat+Defense+API
      - type: Getting Started
        url: https://docs.infoblox.com/space/BloxOneThreatDefense/35369274
      - type: Change Log
        url: https://docs.infoblox.com/display/BloxOneThreatDefense/What's+New+in+Infoblox+Threat+Defense
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox TIDE API
    description: Threat Intelligence Data Exchange (TIDE) API for submitting and retrieving threat indicators. Provides access to indicators of compromise in the TIDE database in multiple formats including JSON, XML, STIX, CEF, and CSV. Used for threat intelligence sharing and enrichment workflows.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://docs.infoblox.com/space/BloxOneThreatDefense/230394127
    baseURL: https://csp.infoblox.com/tide/api
    tags:
      - Indicators
      - Security
      - Threat Intelligence
      - TIDE
    properties:
      - type: Documentation
        url: https://csp.infoblox.com/apidoc/?url=https%3A%2F%2Fcsp.infoblox.com%2Fapidoc%2Fdocs%2FTIDEData
      - type: Getting Started
        url: https://docs.infoblox.com/display/BloxOneThreatDefense/Infoblox+Quick+Start+Guide+for++Dossier+and+TIDE
      - type: Reference
        url: https://docs.infoblox.com/space/BloxOneThreatDefense/230394127/Infoblox+TIDE+API+FAQs+Guide
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox Dossier API
    description: Threat research API that provides contextual information from multiple sources simultaneously for a given indicator. Supports lookups on IPs, URLs, domains, hostnames, email addresses, and file hashes (MD5, SHA1, SHA256) to enrich SIEM and security tool data.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://docs.infoblox.com/display/BloxOneThreatDefense/Dossier+Threat+Research+Portal
    baseURL: https://csp.infoblox.com/tide/api
    tags:
      - Dossier
      - Research
      - Security
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/display/BloxOneThreatDefense/Infoblox+Dossier+User+Guide
      - type: Getting Started
        url: https://docs.infoblox.com/display/BloxOneThreatDefense/Infoblox+Quick+Start+Guide+for++Dossier+and+TIDE
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
  - name: Infoblox NetMRI API
    description: RESTful API for the Infoblox NetMRI network change and configuration management platform. Enables automation of network device provisioning, security compliance checks, configuration management, and network discovery workflows.
    image: https://www.infoblox.com/wp-content/uploads/infoblox-logo.svg
    humanURL: https://www.infoblox.com/products/netmri/
    baseURL: https://{netmri-server}/api
    tags:
      - Compliance
      - Configuration Management
      - Network Automation
    properties:
      - type: Documentation
        url: https://docs.infoblox.com/space/APIDeveloperGuide/43025615/
      - type: Client Libraries
        url: https://github.com/infobloxopen/infoblox-netmri
    contact:
      - FN: Infoblox Support
        email: support@infoblox.com
        url: https://www.infoblox.com/support/
common:
  - type: Portal
    url: https://www.infoblox.com/developer-portal/
  - type: Getting Started
    url: https://www.infoblox.com/developer-portal/getting-started/
  - type: Documentation
    url: https://docs.infoblox.com/
  - type: Blog
    url: https://blogs.infoblox.com/
  - type: Community
    url: https://community.infoblox.com/
  - type: Status
    url: https://status.infoblox.com/
  - type: Support
    url: https://www.infoblox.com/support/
  - type: Website
    url: https://www.infoblox.com/
  - type: Privacy Policy
    url: https://www.infoblox.com/company/legal/privacy-policy/
  - type: Terms of Service
    url: https://www.infoblox.com/company/legal/website-terms-and-conditions/
  - type: GitHub Organization
    url: https://github.com/infobloxopen
  - type: Change Log
    url: https://docs.infoblox.com/space/BloxOneInfrastructure/332366018/BloxOne+Release+Notes
  - type: Console
    url: https://csp.infoblox.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Cloud
  - DDI
  - DHCP
  - DNS
  - IPAM
  - Network Management
  - Security
  - Threat Intelligence
include: []
---
