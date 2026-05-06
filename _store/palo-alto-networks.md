---
aid: palo-alto-networks
name: Palo Alto Networks
description: Palo Alto Networks is a global cybersecurity leader providing advanced security platforms and services across network security, cloud security, and security operations. Its developer platform at pan.dev offers REST and XML APIs for PAN-OS firewalls, Strata Cloud Manager, Prisma Cloud (CSPM, CWPP, code security), Prisma Access and SD-WAN for SASE, Cortex XDR/XSOAR/XSIAM for security operations, and cloud-delivered security services including WildFire, Threat Vault, IoT Security, and DLP.
url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/apis.yml
tags:
  - Cloud Security
  - Cybersecurity
  - Firewall
  - Network Security
  - SASE
  - SOAR
  - Threat Intelligence
  - XDR
created: '2024-01-01'
modified: '2026-04-17'
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
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
      - url: json-schema/pan-os-rest-api-address-group-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-address-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-commit-status-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-nat-rule-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-pan-os-response-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-qos-rule-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-security-rule-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-service-group-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-service-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-tag-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-rest-api-virtual-system-schema.json
        type: JSONSchema
      - url: json-schema/pan-os-security-rule-schema.json
        type: JSONSchema
      - url: json-structure/pan-os-rest-api-address-group-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-address-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-commit-status-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-nat-rule-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-pan-os-response-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-qos-rule-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-security-rule-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-service-group-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-service-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-tag-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-rest-api-virtual-system-structure.json
        type: JSONStructure
      - url: json-structure/pan-os-security-rule-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-pan-os-rest-api-context.jsonld
        type: JSON-LD
      - url: examples/pan-os-rest-api-address-example.json
        type: Example
      - url: examples/pan-os-rest-api-address-group-example.json
        type: Example
      - url: examples/pan-os-rest-api-commit-status-example.json
        type: Example
      - url: examples/pan-os-rest-api-nat-rule-example.json
        type: Example
      - url: examples/pan-os-rest-api-pan-os-response-example.json
        type: Example
      - url: examples/pan-os-rest-api-qos-rule-example.json
        type: Example
      - url: examples/pan-os-rest-api-security-rule-example.json
        type: Example
      - url: examples/pan-os-rest-api-service-example.json
        type: Example
      - url: examples/pan-os-rest-api-service-group-example.json
        type: Example
      - url: examples/pan-os-rest-api-tag-example.json
        type: Example
      - url: examples/pan-os-rest-api-virtual-system-example.json
        type: Example
      - url: examples/pan-os-security-rule-example.json
        type: Example
      - url: json-ld/palo-alto-pan-os-context.jsonld
        type: JSON-LD
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
      - url: https://github.com/PaloAltoNetworks/scm-go
        type: SDK
        title: Go SDK
      - url: json-schema/strata-cloud-manager-api-address-group-list-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-address-group-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-address-group-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-address-list-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-address-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-address-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-delete-response-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-job-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-nat-rule-list-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-nat-rule-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-nat-rule-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-security-rule-list-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-security-rule-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-security-rule-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-service-list-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-service-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-cloud-manager-api-service-schema.json
        type: JSONSchema
      - url: json-structure/strata-cloud-manager-api-address-group-list-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-address-group-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-address-group-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-address-list-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-address-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-address-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-delete-response-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-job-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-nat-rule-list-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-nat-rule-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-nat-rule-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-security-rule-list-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-security-rule-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-security-rule-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-service-list-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-service-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-cloud-manager-api-service-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-strata-cloud-manager-api-context.jsonld
        type: JSON-LD
      - url: examples/strata-cloud-manager-api-address-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-address-group-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-address-group-list-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-address-group-request-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-address-list-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-address-request-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-delete-response-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-job-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-nat-rule-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-nat-rule-list-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-nat-rule-request-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-security-rule-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-security-rule-list-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-security-rule-request-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-service-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-service-list-example.json
        type: Example
      - url: examples/strata-cloud-manager-api-service-request-example.json
        type: Example
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
      - url: json-schema/cloud-ngfw-api-firewall-request-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-firewall-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-firewall-summary-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-fqdn-list-request-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-fqdn-list-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-fqdn-list-summary-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-prefix-list-request-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-prefix-list-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-prefix-list-summary-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-response-status-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-rule-destination-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-rule-source-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-rule-stack-request-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-rule-stack-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-rule-stack-summary-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-security-rule-request-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-security-rule-schema.json
        type: JSONSchema
      - url: json-schema/cloud-ngfw-api-security-rule-summary-schema.json
        type: JSONSchema
      - url: json-structure/cloud-ngfw-api-firewall-request-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-firewall-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-firewall-summary-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-fqdn-list-request-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-fqdn-list-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-fqdn-list-summary-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-prefix-list-request-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-prefix-list-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-prefix-list-summary-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-response-status-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-rule-destination-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-rule-source-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-rule-stack-request-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-rule-stack-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-rule-stack-summary-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-security-rule-request-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-security-rule-structure.json
        type: JSONStructure
      - url: json-structure/cloud-ngfw-api-security-rule-summary-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-cloud-ngfw-api-context.jsonld
        type: JSON-LD
      - url: examples/cloud-ngfw-api-firewall-example.json
        type: Example
      - url: examples/cloud-ngfw-api-firewall-request-example.json
        type: Example
      - url: examples/cloud-ngfw-api-firewall-summary-example.json
        type: Example
      - url: examples/cloud-ngfw-api-fqdn-list-example.json
        type: Example
      - url: examples/cloud-ngfw-api-fqdn-list-request-example.json
        type: Example
      - url: examples/cloud-ngfw-api-fqdn-list-summary-example.json
        type: Example
      - url: examples/cloud-ngfw-api-prefix-list-example.json
        type: Example
      - url: examples/cloud-ngfw-api-prefix-list-request-example.json
        type: Example
      - url: examples/cloud-ngfw-api-prefix-list-summary-example.json
        type: Example
      - url: examples/cloud-ngfw-api-response-status-example.json
        type: Example
      - url: examples/cloud-ngfw-api-rule-destination-example.json
        type: Example
      - url: examples/cloud-ngfw-api-rule-source-example.json
        type: Example
      - url: examples/cloud-ngfw-api-rule-stack-example.json
        type: Example
      - url: examples/cloud-ngfw-api-rule-stack-request-example.json
        type: Example
      - url: examples/cloud-ngfw-api-rule-stack-summary-example.json
        type: Example
      - url: examples/cloud-ngfw-api-security-rule-example.json
        type: Example
      - url: examples/cloud-ngfw-api-security-rule-request-example.json
        type: Example
      - url: examples/cloud-ngfw-api-security-rule-summary-example.json
        type: Example
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
      - url: json-schema/wildfire-api-analysis-report-schema.json
        type: JSONSchema
      - url: json-schema/wildfire-api-bulk-verdict-response-schema.json
        type: JSONSchema
      - url: json-schema/wildfire-api-sandbox-report-schema.json
        type: JSONSchema
      - url: json-schema/wildfire-api-submit-response-schema.json
        type: JSONSchema
      - url: json-schema/wildfire-api-verdict-response-schema.json
        type: JSONSchema
      - url: json-structure/wildfire-api-analysis-report-structure.json
        type: JSONStructure
      - url: json-structure/wildfire-api-bulk-verdict-response-structure.json
        type: JSONStructure
      - url: json-structure/wildfire-api-sandbox-report-structure.json
        type: JSONStructure
      - url: json-structure/wildfire-api-submit-response-structure.json
        type: JSONStructure
      - url: json-structure/wildfire-api-verdict-response-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-wildfire-api-context.jsonld
        type: JSON-LD
      - url: examples/wildfire-api-analysis-report-example.json
        type: Example
      - url: examples/wildfire-api-bulk-verdict-response-example.json
        type: Example
      - url: examples/wildfire-api-sandbox-report-example.json
        type: Example
      - url: examples/wildfire-api-submit-response-example.json
        type: Example
      - url: examples/wildfire-api-verdict-response-example.json
        type: Example
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
      - url: json-schema/threat-vault-api-api-stats-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-atp-report-list-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-atp-report-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-release-note-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-release-notes-list-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-threat-history-entry-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-threat-history-list-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-threat-list-schema.json
        type: JSONSchema
      - url: json-schema/threat-vault-api-threat-signature-schema.json
        type: JSONSchema
      - url: json-structure/threat-vault-api-api-stats-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-atp-report-list-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-atp-report-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-release-note-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-release-notes-list-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-threat-history-entry-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-threat-history-list-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-threat-list-structure.json
        type: JSONStructure
      - url: json-structure/threat-vault-api-threat-signature-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-threat-vault-api-context.jsonld
        type: JSON-LD
      - url: examples/threat-vault-api-api-stats-example.json
        type: Example
      - url: examples/threat-vault-api-atp-report-example.json
        type: Example
      - url: examples/threat-vault-api-atp-report-list-example.json
        type: Example
      - url: examples/threat-vault-api-release-note-example.json
        type: Example
      - url: examples/threat-vault-api-release-notes-list-example.json
        type: Example
      - url: examples/threat-vault-api-threat-history-entry-example.json
        type: Example
      - url: examples/threat-vault-api-threat-history-list-example.json
        type: Example
      - url: examples/threat-vault-api-threat-list-example.json
        type: Example
      - url: examples/threat-vault-api-threat-signature-example.json
        type: Example
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
      - url: json-schema/iot-security-api-alert-schema.json
        type: JSONSchema
      - url: json-schema/iot-security-api-asset-report-schema.json
        type: JSONSchema
      - url: json-schema/iot-security-api-device-schema.json
        type: JSONSchema
      - url: json-schema/iot-security-api-device-tag-schema.json
        type: JSONSchema
      - url: json-schema/iot-security-api-policy-recommendation-schema.json
        type: JSONSchema
      - url: json-schema/iot-security-api-vulnerability-schema.json
        type: JSONSchema
      - url: json-structure/iot-security-api-alert-structure.json
        type: JSONStructure
      - url: json-structure/iot-security-api-asset-report-structure.json
        type: JSONStructure
      - url: json-structure/iot-security-api-device-structure.json
        type: JSONStructure
      - url: json-structure/iot-security-api-device-tag-structure.json
        type: JSONStructure
      - url: json-structure/iot-security-api-policy-recommendation-structure.json
        type: JSONStructure
      - url: json-structure/iot-security-api-vulnerability-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-iot-security-api-context.jsonld
        type: JSON-LD
      - url: examples/iot-security-api-alert-example.json
        type: Example
      - url: examples/iot-security-api-asset-report-example.json
        type: Example
      - url: examples/iot-security-api-device-example.json
        type: Example
      - url: examples/iot-security-api-device-tag-example.json
        type: Example
      - url: examples/iot-security-api-policy-recommendation-example.json
        type: Example
      - url: examples/iot-security-api-vulnerability-example.json
        type: Example
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
      - url: json-schema/dlp-api-content-snippet-schema.json
        type: JSONSchema
      - url: json-schema/dlp-api-data-pattern-schema.json
        type: JSONSchema
      - url: json-schema/dlp-api-dlp-incident-schema.json
        type: JSONSchema
      - url: json-schema/dlp-api-incident-summary-schema.json
        type: JSONSchema
      - url: json-structure/dlp-api-content-snippet-structure.json
        type: JSONStructure
      - url: json-structure/dlp-api-data-pattern-structure.json
        type: JSONStructure
      - url: json-structure/dlp-api-dlp-incident-structure.json
        type: JSONStructure
      - url: json-structure/dlp-api-incident-summary-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-dlp-api-context.jsonld
        type: JSON-LD
      - url: examples/dlp-api-content-snippet-example.json
        type: Example
      - url: examples/dlp-api-data-pattern-example.json
        type: Example
      - url: examples/dlp-api-dlp-incident-example.json
        type: Example
      - url: examples/dlp-api-incident-summary-example.json
        type: Example
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
      - url: json-schema/prisma-access-api-ike-gateway-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-api-ip-sec-tunnel-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-api-job-status-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-api-mobile-agent-infrastructure-settings-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-api-remote-network-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-api-security-rule-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-api-service-connection-schema.json
        type: JSONSchema
      - url: json-structure/prisma-access-api-ike-gateway-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-api-ip-sec-tunnel-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-api-job-status-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-api-mobile-agent-infrastructure-settings-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-api-remote-network-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-api-security-rule-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-api-service-connection-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-access-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-access-api-ike-gateway-example.json
        type: Example
      - url: examples/prisma-access-api-ip-sec-tunnel-example.json
        type: Example
      - url: examples/prisma-access-api-job-status-example.json
        type: Example
      - url: examples/prisma-access-api-mobile-agent-infrastructure-settings-example.json
        type: Example
      - url: examples/prisma-access-api-remote-network-example.json
        type: Example
      - url: examples/prisma-access-api-security-rule-example.json
        type: Example
      - url: examples/prisma-access-api-service-connection-example.json
        type: Example
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
      - url: json-schema/autonomous-dem-api-agent-score-schema.json
        type: JSONSchema
      - url: json-schema/autonomous-dem-api-application-score-schema.json
        type: JSONSchema
      - url: json-schema/autonomous-dem-api-monitored-agent-schema.json
        type: JSONSchema
      - url: json-schema/autonomous-dem-api-monitored-application-schema.json
        type: JSONSchema
      - url: json-schema/autonomous-dem-api-performance-metric-schema.json
        type: JSONSchema
      - url: json-schema/autonomous-dem-api-test-result-schema.json
        type: JSONSchema
      - url: json-structure/autonomous-dem-api-agent-score-structure.json
        type: JSONStructure
      - url: json-structure/autonomous-dem-api-application-score-structure.json
        type: JSONStructure
      - url: json-structure/autonomous-dem-api-monitored-agent-structure.json
        type: JSONStructure
      - url: json-structure/autonomous-dem-api-monitored-application-structure.json
        type: JSONStructure
      - url: json-structure/autonomous-dem-api-performance-metric-structure.json
        type: JSONStructure
      - url: json-structure/autonomous-dem-api-test-result-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-autonomous-dem-api-context.jsonld
        type: JSON-LD
      - url: examples/autonomous-dem-api-agent-score-example.json
        type: Example
      - url: examples/autonomous-dem-api-application-score-example.json
        type: Example
      - url: examples/autonomous-dem-api-monitored-agent-example.json
        type: Example
      - url: examples/autonomous-dem-api-monitored-application-example.json
        type: Example
      - url: examples/autonomous-dem-api-performance-metric-example.json
        type: Example
      - url: examples/autonomous-dem-api-test-result-example.json
        type: Example
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
      - url: json-schema/prisma-sd-wan-api-alarm-schema.json
        type: JSONSchema
      - url: json-schema/prisma-sd-wan-api-application-usage-schema.json
        type: JSONSchema
      - url: json-schema/prisma-sd-wan-api-lan-network-schema.json
        type: JSONSchema
      - url: json-schema/prisma-sd-wan-api-path-rule-schema.json
        type: JSONSchema
      - url: json-schema/prisma-sd-wan-api-qo-s-rule-schema.json
        type: JSONSchema
      - url: json-schema/prisma-sd-wan-api-site-metric-schema.json
        type: JSONSchema
      - url: json-schema/prisma-sd-wan-api-site-schema.json
        type: JSONSchema
      - url: json-schema/prisma-sd-wan-api-wan-interface-schema.json
        type: JSONSchema
      - url: json-structure/prisma-sd-wan-api-alarm-structure.json
        type: JSONStructure
      - url: json-structure/prisma-sd-wan-api-application-usage-structure.json
        type: JSONStructure
      - url: json-structure/prisma-sd-wan-api-lan-network-structure.json
        type: JSONStructure
      - url: json-structure/prisma-sd-wan-api-path-rule-structure.json
        type: JSONStructure
      - url: json-structure/prisma-sd-wan-api-qo-s-rule-structure.json
        type: JSONStructure
      - url: json-structure/prisma-sd-wan-api-site-metric-structure.json
        type: JSONStructure
      - url: json-structure/prisma-sd-wan-api-site-structure.json
        type: JSONStructure
      - url: json-structure/prisma-sd-wan-api-wan-interface-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-sd-wan-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-sd-wan-api-alarm-example.json
        type: Example
      - url: examples/prisma-sd-wan-api-application-usage-example.json
        type: Example
      - url: examples/prisma-sd-wan-api-lan-network-example.json
        type: Example
      - url: examples/prisma-sd-wan-api-path-rule-example.json
        type: Example
      - url: examples/prisma-sd-wan-api-qo-s-rule-example.json
        type: Example
      - url: examples/prisma-sd-wan-api-site-example.json
        type: Example
      - url: examples/prisma-sd-wan-api-site-metric-example.json
        type: Example
      - url: examples/prisma-sd-wan-api-wan-interface-example.json
        type: Example
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
      - url: json-schema/prisma-cloud-cspm-api-alert-filter-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-alert-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-cloud-account-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-compliance-standard-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-policy-input-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-policy-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-report-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-search-result-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-cspm-api-time-range-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-webhooks-alert-payload-schema.json
        type: JSONSchema
      - url: json-structure/prisma-cloud-cspm-api-alert-filter-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-alert-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-cloud-account-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-compliance-standard-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-policy-input-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-policy-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-report-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-search-result-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-cspm-api-time-range-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-policy-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-webhooks-alert-payload-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-cloud-cspm-api-context.jsonld
        type: JSON-LD
      - url: json-ld/palo-alto-prisma-cloud-webhooks-context.jsonld
        type: JSON-LD
      - url: examples/prisma-cloud-cspm-api-alert-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-alert-filter-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-cloud-account-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-compliance-standard-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-policy-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-policy-input-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-report-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-search-result-example.json
        type: Example
      - url: examples/prisma-cloud-cspm-api-time-range-example.json
        type: Example
      - url: examples/prisma-cloud-policy-example.json
        type: Example
      - url: examples/prisma-cloud-webhooks-alert-payload-example.json
        type: Example
      - url: json-ld/palo-alto-prisma-cloud-context.jsonld
        type: JSON-LD
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
      - url: json-schema/prisma-cloud-compute-api-ci-scan-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-compliance-issue-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-compliance-policy-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-container-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-defender-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-defender-summary-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-host-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-image-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-registry-config-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-runtime-policy-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-vulnerability-policy-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-compute-api-vulnerability-schema.json
        type: JSONSchema
      - url: json-structure/prisma-cloud-compute-api-ci-scan-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-compliance-issue-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-compliance-policy-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-container-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-defender-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-defender-summary-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-host-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-image-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-registry-config-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-runtime-policy-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-vulnerability-policy-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-compute-api-vulnerability-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-cloud-compute-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-cloud-compute-api-ci-scan-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-compliance-issue-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-compliance-policy-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-container-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-defender-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-defender-summary-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-host-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-image-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-registry-config-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-runtime-policy-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-vulnerability-example.json
        type: Example
      - url: examples/prisma-cloud-compute-api-vulnerability-policy-example.json
        type: Example
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
      - url: json-schema/prisma-cloud-code-security-api-code-error-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-code-security-api-fix-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-code-security-api-repository-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-code-security-api-scan-integration-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-code-security-api-scan-status-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-code-security-api-suppression-schema.json
        type: JSONSchema
      - url: json-structure/prisma-cloud-code-security-api-code-error-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-code-security-api-fix-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-code-security-api-repository-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-code-security-api-scan-integration-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-code-security-api-scan-status-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-code-security-api-suppression-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-cloud-code-security-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-cloud-code-security-api-code-error-example.json
        type: Example
      - url: examples/prisma-cloud-code-security-api-fix-example.json
        type: Example
      - url: examples/prisma-cloud-code-security-api-repository-example.json
        type: Example
      - url: examples/prisma-cloud-code-security-api-scan-integration-example.json
        type: Example
      - url: examples/prisma-cloud-code-security-api-scan-status-example.json
        type: Example
      - url: examples/prisma-cloud-code-security-api-suppression-example.json
        type: Example
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
      - url: json-schema/cortex-xdr-api-alert-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-api-audit-log-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-api-endpoint-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-api-filter-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-api-incident-detail-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-api-incident-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-api-sort-order-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-webhooks-alert-payload-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xdr-webhooks-incident-payload-schema.json
        type: JSONSchema
      - url: json-structure/cortex-xdr-api-alert-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-api-audit-log-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-api-endpoint-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-api-filter-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-api-incident-detail-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-api-incident-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-api-sort-order-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-incident-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-webhooks-alert-payload-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xdr-webhooks-incident-payload-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-cortex-xdr-api-context.jsonld
        type: JSON-LD
      - url: json-ld/palo-alto-cortex-xdr-webhooks-context.jsonld
        type: JSON-LD
      - url: examples/cortex-xdr-api-alert-example.json
        type: Example
      - url: examples/cortex-xdr-api-audit-log-example.json
        type: Example
      - url: examples/cortex-xdr-api-endpoint-example.json
        type: Example
      - url: examples/cortex-xdr-api-filter-example.json
        type: Example
      - url: examples/cortex-xdr-api-incident-detail-example.json
        type: Example
      - url: examples/cortex-xdr-api-incident-example.json
        type: Example
      - url: examples/cortex-xdr-api-sort-order-example.json
        type: Example
      - url: examples/cortex-xdr-incident-example.json
        type: Example
      - url: examples/cortex-xdr-webhooks-alert-payload-example.json
        type: Example
      - url: examples/cortex-xdr-webhooks-incident-payload-example.json
        type: Example
      - url: json-ld/palo-alto-cortex-xdr-context.jsonld
        type: JSON-LD
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
      - url: json-schema/cortex-xsoar-api-create-entry-request-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-create-incident-request-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-entry-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-incident-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-incident-search-request-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-incident-search-response-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-integration-instance-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-integration-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-investigation-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-playbook-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsoar-api-update-incident-request-schema.json
        type: JSONSchema
      - url: json-structure/cortex-xsoar-api-create-entry-request-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-create-incident-request-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-entry-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-incident-search-request-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-incident-search-response-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-incident-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-integration-instance-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-integration-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-investigation-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-playbook-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-api-update-incident-request-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsoar-integration-manifest-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-cortex-xsoar-api-context.jsonld
        type: JSON-LD
      - url: examples/cortex-xsoar-api-create-entry-request-example.json
        type: Example
      - url: examples/cortex-xsoar-api-create-incident-request-example.json
        type: Example
      - url: examples/cortex-xsoar-api-entry-example.json
        type: Example
      - url: examples/cortex-xsoar-api-incident-example.json
        type: Example
      - url: examples/cortex-xsoar-api-incident-search-request-example.json
        type: Example
      - url: examples/cortex-xsoar-api-incident-search-response-example.json
        type: Example
      - url: examples/cortex-xsoar-api-integration-example.json
        type: Example
      - url: examples/cortex-xsoar-api-integration-instance-example.json
        type: Example
      - url: examples/cortex-xsoar-api-investigation-example.json
        type: Example
      - url: examples/cortex-xsoar-api-playbook-example.json
        type: Example
      - url: examples/cortex-xsoar-api-update-incident-request-example.json
        type: Example
      - url: examples/cortex-xsoar-integration-manifest-example.json
        type: Example
      - url: json-ld/palo-alto-cortex-xsoar-context.jsonld
        type: JSON-LD
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
      - url: json-schema/cortex-xsiam-api-alert-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-api-asset-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-api-audit-log-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-api-endpoint-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-api-filter-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-api-incident-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-api-sort-order-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-data-ingestion-event-data-payload-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-data-ingestion-log-data-payload-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xsiam-data-ingestion-xdr-data-payload-schema.json
        type: JSONSchema
      - url: json-structure/cortex-xsiam-api-alert-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-api-asset-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-api-audit-log-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-api-endpoint-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-api-filter-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-api-incident-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-api-sort-order-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-data-ingestion-event-data-payload-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-data-ingestion-log-data-payload-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xsiam-data-ingestion-xdr-data-payload-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-cortex-xsiam-api-context.jsonld
        type: JSON-LD
      - url: json-ld/palo-alto-cortex-xsiam-data-ingestion-context.jsonld
        type: JSON-LD
      - url: examples/cortex-xsiam-api-alert-example.json
        type: Example
      - url: examples/cortex-xsiam-api-asset-example.json
        type: Example
      - url: examples/cortex-xsiam-api-audit-log-example.json
        type: Example
      - url: examples/cortex-xsiam-api-endpoint-example.json
        type: Example
      - url: examples/cortex-xsiam-api-filter-example.json
        type: Example
      - url: examples/cortex-xsiam-api-incident-example.json
        type: Example
      - url: examples/cortex-xsiam-api-sort-order-example.json
        type: Example
      - url: examples/cortex-xsiam-data-ingestion-event-data-payload-example.json
        type: Example
      - url: examples/cortex-xsiam-data-ingestion-log-data-payload-example.json
        type: Example
      - url: examples/cortex-xsiam-data-ingestion-xdr-data-payload-example.json
        type: Example
    description: A REST API for Cortex XSIAM, the AI-driven security operations platform that combines SIEM, XDR, SOAR, and ASM capabilities. The API provides endpoints for incident management, alert handling, data ingestion configuration, XQL query execution, asset management, and automation rule management. Shares endpoint patterns with Cortex XDR but includes additional capabilities for log collection configuration, data model management, and AI-assisted investigation.
  - aid: palo-alto-networks:prisma-airs-api
    name: Prisma AIRS AI Runtime Security API
    tags:
      - AI Runtime
      - AI Security
      - API Intercept
      - GenAI
      - LLM Security
      - MCP Security
      - Prompt Injection
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://service.api.aisecurity.paloaltonetworks.com
    humanURL: https://pan.dev/airs/
    properties:
      - url: https://pan.dev/airs/
        type: Documentation
      - url: https://pan.dev/prisma-airs/api/airuntimesecurity/airuntimesecurityapi/
        type: APIReference
      - url: https://docs.paloaltonetworks.com/ai-runtime-security/activation-and-onboarding/ai-runtime-security-api-intercept-overview
        type: GettingStarted
      - url: https://pan.dev/prisma-airs/api/airuntimesecurity/pythonsdk/
        type: SDK
        title: Python SDK
      - url: https://github.com/PaloAltoNetworks/aisecurity-python-sdk
        type: GitHubRepository
      - url: https://github.com/PaloAltoNetworks/airs-api-mgmt-sdk
        type: SDK
        title: AIRS Management Python SDK
      - url: openapi/palo-alto-prisma-airs-api-openapi-original.yml
        type: OpenAPI
      - url: json-schema/prisma-airs-api-ai-profile-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-api-content-scan-result-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-api-scan-content-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-api-scan-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-api-scan-response-schema.json
        type: JSONSchema
      - url: json-structure/prisma-airs-api-ai-profile-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-api-content-scan-result-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-api-scan-content-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-api-scan-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-api-scan-response-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-airs-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-airs-api-ai-profile-example.json
        type: Example
      - url: examples/prisma-airs-api-content-scan-result-example.json
        type: Example
      - url: examples/prisma-airs-api-scan-content-example.json
        type: Example
      - url: examples/prisma-airs-api-scan-request-example.json
        type: Example
      - url: examples/prisma-airs-api-scan-response-example.json
        type: Example
    description: The AI Runtime Security API (API Intercept) for securing generative AI applications, AI models, AI data, and AI agents against prompt injection, data leakage, toxic content, malicious URLs, database security attacks, malicious code, and other AI-specific threats. Provides Scan APIs for real-time threat detection on prompts and model responses, and Management APIs for configuring security profiles, API keys, and deployments. Supports Secure MCP, custom topic guardrails, contextual grounding, and data masking. Available in US, EU (Germany), India, and Singapore regions. Integrates via REST API or the pan-aisecurity Python SDK with API key or OAuth 2.0 authentication.
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
      - url: json-schema/security-advisory-api-advisory-schema.json
        type: JSONSchema
      - url: json-schema/security-advisory-api-affected-product-schema.json
        type: JSONSchema
      - url: json-schema/security-advisory-api-product-schema.json
        type: JSONSchema
      - url: json-structure/palo-alto-security-advisory-structure.json
        type: JSONStructure
      - url: json-structure/security-advisory-api-advisory-structure.json
        type: JSONStructure
      - url: json-structure/security-advisory-api-affected-product-structure.json
        type: JSONStructure
      - url: json-structure/security-advisory-api-product-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-security-advisory-api-context.jsonld
        type: JSON-LD
      - url: json-ld/palo-alto-security-advisory-context.jsonld
        type: JSON-LD
      - url: examples/palo-alto-security-advisory-example.json
        type: Example
      - url: examples/security-advisory-api-advisory-example.json
        type: Example
      - url: examples/security-advisory-api-affected-product-example.json
        type: Example
      - url: examples/security-advisory-api-product-example.json
        type: Example
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
      - url: json-schema/cortex-xpanse-api-asm-incident-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-asset-internet-exposure-detail-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-asset-internet-exposure-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-attack-surface-rule-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-audit-log-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-exposed-service-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-filter-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-owned-ip-range-schema.json
        type: JSONSchema
      - url: json-schema/cortex-xpanse-api-sort-order-schema.json
        type: JSONSchema
      - url: json-structure/cortex-xpanse-api-asm-incident-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-asset-internet-exposure-detail-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-asset-internet-exposure-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-attack-surface-rule-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-audit-log-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-exposed-service-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-filter-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-owned-ip-range-structure.json
        type: JSONStructure
      - url: json-structure/cortex-xpanse-api-sort-order-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-cortex-xpanse-api-context.jsonld
        type: JSON-LD
      - url: examples/cortex-xpanse-api-asm-incident-example.json
        type: Example
      - url: examples/cortex-xpanse-api-asset-internet-exposure-detail-example.json
        type: Example
      - url: examples/cortex-xpanse-api-asset-internet-exposure-example.json
        type: Example
      - url: examples/cortex-xpanse-api-attack-surface-rule-example.json
        type: Example
      - url: examples/cortex-xpanse-api-audit-log-example.json
        type: Example
      - url: examples/cortex-xpanse-api-exposed-service-example.json
        type: Example
      - url: examples/cortex-xpanse-api-filter-example.json
        type: Example
      - url: examples/cortex-xpanse-api-owned-ip-range-example.json
        type: Example
      - url: examples/cortex-xpanse-api-sort-order-example.json
        type: Example
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
      - url: json-schema/dns-security-api-domain-detail-schema.json
        type: JSONSchema
      - url: json-schema/dns-security-api-network-stats-schema.json
        type: JSONSchema
      - url: json-structure/dns-security-api-domain-detail-structure.json
        type: JSONStructure
      - url: json-structure/dns-security-api-network-stats-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-dns-security-api-context.jsonld
        type: JSON-LD
      - url: examples/dns-security-api-domain-detail-example.json
        type: Example
      - url: examples/dns-security-api-network-stats-example.json
        type: Example
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
      - url: json-schema/email-dlp-api-email-attachment-schema.json
        type: JSONSchema
      - url: json-schema/email-dlp-api-email-dlp-incident-schema.json
        type: JSONSchema
      - url: json-schema/email-dlp-api-email-recipient-schema.json
        type: JSONSchema
      - url: json-structure/email-dlp-api-email-attachment-structure.json
        type: JSONStructure
      - url: json-structure/email-dlp-api-email-dlp-incident-structure.json
        type: JSONStructure
      - url: json-structure/email-dlp-api-email-recipient-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-email-dlp-api-context.jsonld
        type: JSON-LD
      - url: examples/email-dlp-api-email-attachment-example.json
        type: Example
      - url: examples/email-dlp-api-email-dlp-incident-example.json
        type: Example
      - url: examples/email-dlp-api-email-recipient-example.json
        type: Example
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
      - url: json-schema/saas-security-api-application-schema.json
        type: JSONSchema
      - url: json-schema/saas-security-api-asset-schema.json
        type: JSONSchema
      - url: json-schema/saas-security-api-incident-schema.json
        type: JSONSchema
      - url: json-schema/saas-security-api-log-forwarding-settings-schema.json
        type: JSONSchema
      - url: json-schema/saas-security-api-user-activity-schema.json
        type: JSONSchema
      - url: json-schema/saas-security-api-user-schema.json
        type: JSONSchema
      - url: json-structure/saas-security-api-application-structure.json
        type: JSONStructure
      - url: json-structure/saas-security-api-asset-structure.json
        type: JSONStructure
      - url: json-structure/saas-security-api-incident-structure.json
        type: JSONStructure
      - url: json-structure/saas-security-api-log-forwarding-settings-structure.json
        type: JSONStructure
      - url: json-structure/saas-security-api-user-activity-structure.json
        type: JSONStructure
      - url: json-structure/saas-security-api-user-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-saas-security-api-context.jsonld
        type: JSON-LD
      - url: examples/saas-security-api-application-example.json
        type: Example
      - url: examples/saas-security-api-asset-example.json
        type: Example
      - url: examples/saas-security-api-incident-example.json
        type: Example
      - url: examples/saas-security-api-log-forwarding-settings-example.json
        type: Example
      - url: examples/saas-security-api-user-activity-example.json
        type: Example
      - url: examples/saas-security-api-user-example.json
        type: Example
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
      - url: json-schema/sspm-api-catalog-app-schema.json
        type: JSONSchema
      - url: json-schema/sspm-api-jira-integration-request-schema.json
        type: JSONSchema
      - url: json-schema/sspm-api-jira-integration-schema.json
        type: JSONSchema
      - url: json-schema/sspm-api-onboard-app-request-schema.json
        type: JSONSchema
      - url: json-schema/sspm-api-onboarded-app-schema.json
        type: JSONSchema
      - url: json-schema/sspm-api-posture-check-schema.json
        type: JSONSchema
      - url: json-structure/sspm-api-catalog-app-structure.json
        type: JSONStructure
      - url: json-structure/sspm-api-jira-integration-request-structure.json
        type: JSONStructure
      - url: json-structure/sspm-api-jira-integration-structure.json
        type: JSONStructure
      - url: json-structure/sspm-api-onboard-app-request-structure.json
        type: JSONStructure
      - url: json-structure/sspm-api-onboarded-app-structure.json
        type: JSONStructure
      - url: json-structure/sspm-api-posture-check-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sspm-api-context.jsonld
        type: JSON-LD
      - url: examples/sspm-api-catalog-app-example.json
        type: Example
      - url: examples/sspm-api-jira-integration-example.json
        type: Example
      - url: examples/sspm-api-jira-integration-request-example.json
        type: Example
      - url: examples/sspm-api-onboard-app-request-example.json
        type: Example
      - url: examples/sspm-api-onboarded-app-example.json
        type: Example
      - url: examples/sspm-api-posture-check-example.json
        type: Example
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
      - url: json-schema/ztna-connector-api-connector-group-request-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-connector-group-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-connector-request-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-connector-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-fqdn-rule-request-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-fqdn-rule-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-license-info-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-subnet-rule-request-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-subnet-rule-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-ztna-application-request-schema.json
        type: JSONSchema
      - url: json-schema/ztna-connector-api-ztna-application-schema.json
        type: JSONSchema
      - url: json-structure/ztna-connector-api-connector-group-request-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-connector-group-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-connector-request-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-connector-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-fqdn-rule-request-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-fqdn-rule-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-license-info-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-subnet-rule-request-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-subnet-rule-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-ztna-application-request-structure.json
        type: JSONStructure
      - url: json-structure/ztna-connector-api-ztna-application-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-ztna-connector-api-context.jsonld
        type: JSON-LD
      - url: examples/ztna-connector-api-connector-example.json
        type: Example
      - url: examples/ztna-connector-api-connector-group-example.json
        type: Example
      - url: examples/ztna-connector-api-connector-group-request-example.json
        type: Example
      - url: examples/ztna-connector-api-connector-request-example.json
        type: Example
      - url: examples/ztna-connector-api-fqdn-rule-example.json
        type: Example
      - url: examples/ztna-connector-api-fqdn-rule-request-example.json
        type: Example
      - url: examples/ztna-connector-api-license-info-example.json
        type: Example
      - url: examples/ztna-connector-api-subnet-rule-example.json
        type: Example
      - url: examples/ztna-connector-api-subnet-rule-request-example.json
        type: Example
      - url: examples/ztna-connector-api-ztna-application-example.json
        type: Example
      - url: examples/ztna-connector-api-ztna-application-request-example.json
        type: Example
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
      - url: json-schema/prisma-access-browser-api-browser-deployment-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-browser-api-browser-deployment-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-browser-api-browser-policy-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-browser-api-browser-policy-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-browser-api-browser-session-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-browser-api-browser-user-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-browser-api-managed-device-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-browser-api-usage-report-schema.json
        type: JSONSchema
      - url: json-structure/prisma-access-browser-api-browser-deployment-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-browser-api-browser-deployment-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-browser-api-browser-policy-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-browser-api-browser-policy-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-browser-api-browser-session-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-browser-api-browser-user-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-browser-api-managed-device-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-browser-api-usage-report-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-access-browser-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-access-browser-api-browser-deployment-example.json
        type: Example
      - url: examples/prisma-access-browser-api-browser-deployment-request-example.json
        type: Example
      - url: examples/prisma-access-browser-api-browser-policy-example.json
        type: Example
      - url: examples/prisma-access-browser-api-browser-policy-request-example.json
        type: Example
      - url: examples/prisma-access-browser-api-browser-session-example.json
        type: Example
      - url: examples/prisma-access-browser-api-browser-user-example.json
        type: Example
      - url: examples/prisma-access-browser-api-managed-device-example.json
        type: Example
      - url: examples/prisma-access-browser-api-usage-report-example.json
        type: Example
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
      - url: json-schema/sase-tenancy-api-tenant-service-group-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-tenancy-api-tenant-service-group-schema.json
        type: JSONSchema
      - url: json-schema/sase-tenancy-api-tenant-service-group-update-schema.json
        type: JSONSchema
      - url: json-structure/sase-tenancy-api-tenant-service-group-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-tenancy-api-tenant-service-group-structure.json
        type: JSONStructure
      - url: json-structure/sase-tenancy-api-tenant-service-group-update-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-tenancy-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-tenancy-api-tenant-service-group-example.json
        type: Example
      - url: examples/sase-tenancy-api-tenant-service-group-request-example.json
        type: Example
      - url: examples/sase-tenancy-api-tenant-service-group-update-example.json
        type: Example
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
      - url: json-schema/sase-iam-api-access-policy-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-iam-api-access-policy-schema.json
        type: JSONSchema
      - url: json-schema/sase-iam-api-role-schema.json
        type: JSONSchema
      - url: json-schema/sase-iam-api-service-account-credentials-schema.json
        type: JSONSchema
      - url: json-schema/sase-iam-api-service-account-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-iam-api-service-account-schema.json
        type: JSONSchema
      - url: json-schema/sase-iam-api-service-account-update-schema.json
        type: JSONSchema
      - url: json-structure/sase-iam-api-access-policy-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-iam-api-access-policy-structure.json
        type: JSONStructure
      - url: json-structure/sase-iam-api-role-structure.json
        type: JSONStructure
      - url: json-structure/sase-iam-api-service-account-credentials-structure.json
        type: JSONStructure
      - url: json-structure/sase-iam-api-service-account-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-iam-api-service-account-structure.json
        type: JSONStructure
      - url: json-structure/sase-iam-api-service-account-update-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-iam-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-iam-api-access-policy-example.json
        type: Example
      - url: examples/sase-iam-api-access-policy-request-example.json
        type: Example
      - url: examples/sase-iam-api-role-example.json
        type: Example
      - url: examples/sase-iam-api-service-account-credentials-example.json
        type: Example
      - url: examples/sase-iam-api-service-account-example.json
        type: Example
      - url: examples/sase-iam-api-service-account-request-example.json
        type: Example
      - url: examples/sase-iam-api-service-account-update-example.json
        type: Example
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
      - url: json-schema/sase-subscription-api-allocation-entry-schema.json
        type: JSONSchema
      - url: json-schema/sase-subscription-api-allocation-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-subscription-api-entitlement-schema.json
        type: JSONSchema
      - url: json-schema/sase-subscription-api-subscription-entitlements-schema.json
        type: JSONSchema
      - url: json-schema/sase-subscription-api-subscription-schema.json
        type: JSONSchema
      - url: json-structure/sase-subscription-api-allocation-entry-structure.json
        type: JSONStructure
      - url: json-structure/sase-subscription-api-allocation-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-subscription-api-entitlement-structure.json
        type: JSONStructure
      - url: json-structure/sase-subscription-api-subscription-entitlements-structure.json
        type: JSONStructure
      - url: json-structure/sase-subscription-api-subscription-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-subscription-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-subscription-api-allocation-entry-example.json
        type: Example
      - url: examples/sase-subscription-api-allocation-request-example.json
        type: Example
      - url: examples/sase-subscription-api-entitlement-example.json
        type: Example
      - url: examples/sase-subscription-api-subscription-entitlements-example.json
        type: Example
      - url: examples/sase-subscription-api-subscription-example.json
        type: Example
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
      - url: json-schema/sase-aggregate-monitoring-api-aggregation-query-schema.json
        type: JSONSchema
      - url: json-schema/sase-aggregate-monitoring-api-aggregation-response-schema.json
        type: JSONSchema
      - url: json-schema/sase-aggregate-monitoring-api-tenant-summary-schema.json
        type: JSONSchema
      - url: json-structure/sase-aggregate-monitoring-api-aggregation-query-structure.json
        type: JSONStructure
      - url: json-structure/sase-aggregate-monitoring-api-aggregation-response-structure.json
        type: JSONStructure
      - url: json-structure/sase-aggregate-monitoring-api-tenant-summary-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-aggregate-monitoring-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-aggregate-monitoring-api-aggregation-query-example.json
        type: Example
      - url: examples/sase-aggregate-monitoring-api-aggregation-response-example.json
        type: Example
      - url: examples/sase-aggregate-monitoring-api-tenant-summary-example.json
        type: Example
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
      - url: json-schema/aiops-ngfw-bpa-api-bpa-check-schema.json
        type: JSONSchema
      - url: json-schema/aiops-ngfw-bpa-api-bpa-report-schema.json
        type: JSONSchema
      - url: json-schema/aiops-ngfw-bpa-api-bpa-request-schema.json
        type: JSONSchema
      - url: json-schema/aiops-ngfw-bpa-api-bpa-request-status-schema.json
        type: JSONSchema
      - url: json-structure/aiops-ngfw-bpa-api-bpa-check-structure.json
        type: JSONStructure
      - url: json-structure/aiops-ngfw-bpa-api-bpa-report-structure.json
        type: JSONStructure
      - url: json-structure/aiops-ngfw-bpa-api-bpa-request-status-structure.json
        type: JSONStructure
      - url: json-structure/aiops-ngfw-bpa-api-bpa-request-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-aiops-ngfw-bpa-api-context.jsonld
        type: JSON-LD
      - url: examples/aiops-ngfw-bpa-api-bpa-check-example.json
        type: Example
      - url: examples/aiops-ngfw-bpa-api-bpa-report-example.json
        type: Example
      - url: examples/aiops-ngfw-bpa-api-bpa-request-example.json
        type: Example
      - url: examples/aiops-ngfw-bpa-api-bpa-request-status-example.json
        type: Example
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
      - url: json-schema/strata-logging-forwarding-auth-log-payload-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-forwarding-threat-log-payload-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-forwarding-traffic-log-payload-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-forwarding-url-log-payload-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-forwarding-wildfire-log-payload-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-email-destination-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-email-destination-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-forwarding-status-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-https-destination-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-https-destination-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-log-forwarding-profile-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-log-forwarding-profile-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-syslog-destination-request-schema.json
        type: JSONSchema
      - url: json-schema/strata-logging-service-api-syslog-destination-schema.json
        type: JSONSchema
      - url: json-structure/strata-logging-forwarding-auth-log-payload-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-forwarding-threat-log-payload-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-forwarding-traffic-log-payload-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-forwarding-url-log-payload-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-forwarding-wildfire-log-payload-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-email-destination-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-email-destination-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-forwarding-status-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-https-destination-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-https-destination-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-log-forwarding-profile-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-log-forwarding-profile-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-syslog-destination-request-structure.json
        type: JSONStructure
      - url: json-structure/strata-logging-service-api-syslog-destination-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-strata-logging-forwarding-context.jsonld
        type: JSON-LD
      - url: json-ld/palo-alto-strata-logging-service-api-context.jsonld
        type: JSON-LD
      - url: examples/strata-logging-forwarding-auth-log-payload-example.json
        type: Example
      - url: examples/strata-logging-forwarding-threat-log-payload-example.json
        type: Example
      - url: examples/strata-logging-forwarding-traffic-log-payload-example.json
        type: Example
      - url: examples/strata-logging-forwarding-url-log-payload-example.json
        type: Example
      - url: examples/strata-logging-forwarding-wildfire-log-payload-example.json
        type: Example
      - url: examples/strata-logging-service-api-email-destination-example.json
        type: Example
      - url: examples/strata-logging-service-api-email-destination-request-example.json
        type: Example
      - url: examples/strata-logging-service-api-forwarding-status-example.json
        type: Example
      - url: examples/strata-logging-service-api-https-destination-example.json
        type: Example
      - url: examples/strata-logging-service-api-https-destination-request-example.json
        type: Example
      - url: examples/strata-logging-service-api-log-forwarding-profile-example.json
        type: Example
      - url: examples/strata-logging-service-api-log-forwarding-profile-request-example.json
        type: Example
      - url: examples/strata-logging-service-api-syslog-destination-example.json
        type: Example
      - url: examples/strata-logging-service-api-syslog-destination-request-example.json
        type: Example
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
      - url: json-schema/sase-config-orchestration-api-bandwidth-allocation-schema.json
        type: JSONSchema
      - url: json-schema/sase-config-orchestration-api-i-psec-tunnel-schema.json
        type: JSONSchema
      - url: json-schema/sase-config-orchestration-api-ike-gateway-config-schema.json
        type: JSONSchema
      - url: json-schema/sase-config-orchestration-api-ike-gateway-schema.json
        type: JSONSchema
      - url: json-schema/sase-config-orchestration-api-onboarding-status-schema.json
        type: JSONSchema
      - url: json-schema/sase-config-orchestration-api-prisma-access-location-schema.json
        type: JSONSchema
      - url: json-schema/sase-config-orchestration-api-remote-network-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-config-orchestration-api-remote-network-schema.json
        type: JSONSchema
      - url: json-structure/sase-config-orchestration-api-bandwidth-allocation-structure.json
        type: JSONStructure
      - url: json-structure/sase-config-orchestration-api-i-psec-tunnel-structure.json
        type: JSONStructure
      - url: json-structure/sase-config-orchestration-api-ike-gateway-config-structure.json
        type: JSONStructure
      - url: json-structure/sase-config-orchestration-api-ike-gateway-structure.json
        type: JSONStructure
      - url: json-structure/sase-config-orchestration-api-onboarding-status-structure.json
        type: JSONStructure
      - url: json-structure/sase-config-orchestration-api-prisma-access-location-structure.json
        type: JSONStructure
      - url: json-structure/sase-config-orchestration-api-remote-network-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-config-orchestration-api-remote-network-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-config-orchestration-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-config-orchestration-api-bandwidth-allocation-example.json
        type: Example
      - url: examples/sase-config-orchestration-api-i-psec-tunnel-example.json
        type: Example
      - url: examples/sase-config-orchestration-api-ike-gateway-config-example.json
        type: Example
      - url: examples/sase-config-orchestration-api-ike-gateway-example.json
        type: Example
      - url: examples/sase-config-orchestration-api-onboarding-status-example.json
        type: Example
      - url: examples/sase-config-orchestration-api-prisma-access-location-example.json
        type: Example
      - url: examples/sase-config-orchestration-api-remote-network-example.json
        type: Example
      - url: examples/sase-config-orchestration-api-remote-network-request-example.json
        type: Example
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
      - url: json-schema/prisma-cloud-dspm-api-classification-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-dspm-api-data-asset-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-dspm-api-data-risk-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-dspm-api-data-security-alert-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-dspm-api-data-store-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-dspm-api-dspm-policy-schema.json
        type: JSONSchema
      - url: json-structure/prisma-cloud-dspm-api-classification-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-dspm-api-data-asset-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-dspm-api-data-risk-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-dspm-api-data-security-alert-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-dspm-api-data-store-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-dspm-api-dspm-policy-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-cloud-dspm-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-cloud-dspm-api-classification-example.json
        type: Example
      - url: examples/prisma-cloud-dspm-api-data-asset-example.json
        type: Example
      - url: examples/prisma-cloud-dspm-api-data-risk-example.json
        type: Example
      - url: examples/prisma-cloud-dspm-api-data-security-alert-example.json
        type: Example
      - url: examples/prisma-cloud-dspm-api-data-store-example.json
        type: Example
      - url: examples/prisma-cloud-dspm-api-dspm-policy-example.json
        type: Example
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
      - url: json-schema/sase-5g-api-network-slice-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-api-network-slice-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-api-security-metrics5-g-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-api-security-policy5-g-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-api-security-policy5-g-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-api-tenant5-g-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-api-tenant5-g-schema.json
        type: JSONSchema
      - url: json-structure/sase-5g-api-network-slice-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-api-network-slice-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-api-security-metrics5-g-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-api-security-policy5-g-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-api-security-policy5-g-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-api-tenant5-g-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-api-tenant5-g-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-5g-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-5g-api-network-slice-example.json
        type: Example
      - url: examples/sase-5g-api-network-slice-request-example.json
        type: Example
      - url: examples/sase-5g-api-security-metrics5-g-example.json
        type: Example
      - url: examples/sase-5g-api-security-policy5-g-example.json
        type: Example
      - url: examples/sase-5g-api-security-policy5-g-request-example.json
        type: Example
      - url: examples/sase-5g-api-tenant5-g-example.json
        type: Example
      - url: examples/sase-5g-api-tenant5-g-request-example.json
        type: Example
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
      - url: json-schema/prisma-airs-ai-red-teaming-api-attack-category-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-ai-red-teaming-api-scan-report-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-ai-red-teaming-api-scan-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-ai-red-teaming-api-scan-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-ai-red-teaming-api-scan-target-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-ai-red-teaming-api-scan-target-schema.json
        type: JSONSchema
      - url: json-schema/prisma-airs-ai-red-teaming-api-vulnerability-finding-schema.json
        type: JSONSchema
      - url: json-structure/prisma-airs-ai-red-teaming-api-attack-category-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-ai-red-teaming-api-scan-report-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-ai-red-teaming-api-scan-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-ai-red-teaming-api-scan-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-ai-red-teaming-api-scan-target-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-ai-red-teaming-api-scan-target-structure.json
        type: JSONStructure
      - url: json-structure/prisma-airs-ai-red-teaming-api-vulnerability-finding-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-airs-ai-red-teaming-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-airs-ai-red-teaming-api-attack-category-example.json
        type: Example
      - url: examples/prisma-airs-ai-red-teaming-api-scan-example.json
        type: Example
      - url: examples/prisma-airs-ai-red-teaming-api-scan-report-example.json
        type: Example
      - url: examples/prisma-airs-ai-red-teaming-api-scan-request-example.json
        type: Example
      - url: examples/prisma-airs-ai-red-teaming-api-scan-target-example.json
        type: Example
      - url: examples/prisma-airs-ai-red-teaming-api-scan-target-request-example.json
        type: Example
      - url: examples/prisma-airs-ai-red-teaming-api-vulnerability-finding-example.json
        type: Example
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
      - url: openapi/palo-alto-identity-security-posture-management-api-openapi-original.yml
        type: OpenAPI
      - url: json-schema/identity-security-posture-management-api-create-ticket-request-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-download-csv-request-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-feature-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-feature-state-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-idp-info-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-instant-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-list-response-idp-info-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-list-response-map-string-object-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-list-response-mfa-activity-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-list-response-saa-s-account-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-list-response-saa-s-activity-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-list-response-saa-s-instance-info-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-list-response-ticket-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-mfa-activity-count-by-app-type-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-mfa-activity-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-remediation-request-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-saa-s-account-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-saa-s-activity-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-saa-s-instance-info-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-ticket-schema.json
        type: JSONSchema
      - url: json-schema/identity-security-posture-management-api-unlink-ticket-request-schema.json
        type: JSONSchema
      - url: json-structure/identity-security-posture-management-api-create-ticket-request-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-download-csv-request-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-feature-state-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-feature-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-idp-info-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-instant-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-list-response-idp-info-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-list-response-map-string-object-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-list-response-mfa-activity-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-list-response-saa-s-account-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-list-response-saa-s-activity-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-list-response-saa-s-instance-info-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-list-response-ticket-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-mfa-activity-count-by-app-type-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-mfa-activity-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-remediation-request-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-saa-s-account-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-saa-s-activity-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-saa-s-instance-info-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-ticket-structure.json
        type: JSONStructure
      - url: json-structure/identity-security-posture-management-api-unlink-ticket-request-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-identity-security-posture-management-api-context.jsonld
        type: JSON-LD
      - url: examples/identity-security-posture-management-api-create-ticket-request-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-download-csv-request-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-feature-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-feature-state-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-idp-info-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-instant-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-list-response-idp-info-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-list-response-map-string-object-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-list-response-mfa-activity-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-list-response-saa-s-account-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-list-response-saa-s-activity-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-list-response-saa-s-instance-info-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-list-response-ticket-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-mfa-activity-count-by-app-type-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-mfa-activity-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-remediation-request-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-saa-s-account-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-saa-s-activity-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-saa-s-instance-info-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-ticket-example.json
        type: Example
      - url: examples/identity-security-posture-management-api-unlink-ticket-request-example.json
        type: Example
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
      - url: openapi/palo-alto-sase-5g-monitor-api-openapi-original.yml
        type: OpenAPI
      - url: json-schema/sase-5g-monitor-api-count-filter-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-monitor-api-incidents-count-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-monitor-api-mapping-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-monitor-api-throughput-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-5g-monitor-api-trend-request-schema.json
        type: JSONSchema
      - url: json-structure/sase-5g-monitor-api-count-filter-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-monitor-api-incidents-count-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-monitor-api-mapping-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-monitor-api-throughput-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-5g-monitor-api-trend-request-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-5g-monitor-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-5g-monitor-api-count-filter-request-example.json
        type: Example
      - url: examples/sase-5g-monitor-api-incidents-count-request-example.json
        type: Example
      - url: examples/sase-5g-monitor-api-mapping-request-example.json
        type: Example
      - url: examples/sase-5g-monitor-api-throughput-request-example.json
        type: Example
      - url: examples/sase-5g-monitor-api-trend-request-example.json
        type: Example
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
      - url: openapi/palo-alto-sase-multitenant-notifications-api-openapi-original.yml
        type: OpenAPI
      - url: json-schema/sase-multitenant-notifications-api-email-channel-details-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-email-details-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-mt-notif-agg-key-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-mt-notification-list-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-mt-notification-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-category-detail-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-channel-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-filter-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-list-api-req-body-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-profile-list-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-profile-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-read-state-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-state-change-api-body-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-sub-category-detail-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-notif-type-detail-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-sort-by-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-notifications-api-webhook-channel-details-schema.json
        type: JSONSchema
      - url: json-structure/sase-multitenant-notifications-api-email-channel-details-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-email-details-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-mt-notif-agg-key-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-mt-notification-list-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-mt-notification-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-category-detail-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-channel-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-filter-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-list-api-req-body-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-profile-list-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-profile-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-read-state-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-state-change-api-body-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-sub-category-detail-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-notif-type-detail-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-sort-by-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-notifications-api-webhook-channel-details-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-multitenant-notifications-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-multitenant-notifications-api-email-channel-details-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-email-details-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-mt-notif-agg-key-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-mt-notification-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-mt-notification-list-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-category-detail-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-channel-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-filter-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-list-api-req-body-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-profile-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-profile-list-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-read-state-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-state-change-api-body-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-sub-category-detail-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-notif-type-detail-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-sort-by-example.json
        type: Example
      - url: examples/sase-multitenant-notifications-api-webhook-channel-details-example.json
        type: Example
      - url: json-schema/sase-notifications-announcement-notification-schema.json
        type: JSONSchema
      - url: json-schema/sase-notifications-certificate-expiry-notification-schema.json
        type: JSONSchema
      - url: json-schema/sase-notifications-dataplane-upgrade-notification-schema.json
        type: JSONSchema
      - url: json-schema/sase-notifications-incident-detail-schema.json
        type: JSONSchema
      - url: json-schema/sase-notifications-incident-notification-schema.json
        type: JSONSchema
      - url: json-schema/sase-notifications-service-info-schema.json
        type: JSONSchema
      - url: json-schema/sase-notifications-tenant-context-schema.json
        type: JSONSchema
      - url: json-structure/sase-notifications-announcement-notification-structure.json
        type: JSONStructure
      - url: json-structure/sase-notifications-certificate-expiry-notification-structure.json
        type: JSONStructure
      - url: json-structure/sase-notifications-dataplane-upgrade-notification-structure.json
        type: JSONStructure
      - url: json-structure/sase-notifications-incident-detail-structure.json
        type: JSONStructure
      - url: json-structure/sase-notifications-incident-notification-structure.json
        type: JSONStructure
      - url: json-structure/sase-notifications-service-info-structure.json
        type: JSONStructure
      - url: json-structure/sase-notifications-tenant-context-structure.json
        type: JSONStructure
      - url: examples/sase-notifications-announcement-notification-example.json
        type: Example
      - url: examples/sase-notifications-certificate-expiry-notification-example.json
        type: Example
      - url: examples/sase-notifications-dataplane-upgrade-notification-example.json
        type: Example
      - url: examples/sase-notifications-incident-detail-example.json
        type: Example
      - url: examples/sase-notifications-incident-notification-example.json
        type: Example
      - url: examples/sase-notifications-service-info-example.json
        type: Example
      - url: examples/sase-notifications-tenant-context-example.json
        type: Example
      - url: json-ld/palo-alto-sase-notifications-context.jsonld
        type: JSON-LD
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
      - url: openapi/palo-alto-sase-multitenant-interconnect-api-openapi-original.yml
        type: OpenAPI
      - url: json-schema/sase-multitenant-interconnect-api-bandwidth-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-cloud-provider-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-connection-type-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-dedicated-vlan-attachment-details-entry-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-interconnect-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-interconnect-usage-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-ip-block-entry-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-ip-block-type-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-ip-pool-request-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-ip-provider-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-physical-connection-entry-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-physical-interconnect-link-type-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-session-initialization-mode-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-settings-entry-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-stack-type-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address-schema.json
        type: JSONSchema
      - url: json-schema/sase-multitenant-interconnect-api-vlan-attachment-request-schema.json
        type: JSONSchema
      - url: json-structure/sase-multitenant-interconnect-api-bandwidth-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-cloud-provider-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-connection-type-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-dedicated-vlan-attachment-details-entry-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-interconnect-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-interconnect-usage-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-ip-block-entry-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-ip-block-type-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-ip-pool-request-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-ip-provider-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-physical-connection-entry-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-physical-interconnect-link-type-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-session-initialization-mode-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-settings-entry-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-stack-type-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address-structure.json
        type: JSONStructure
      - url: json-structure/sase-multitenant-interconnect-api-vlan-attachment-request-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-sase-multitenant-interconnect-api-context.jsonld
        type: JSON-LD
      - url: examples/sase-multitenant-interconnect-api-bandwidth-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-cloud-provider-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-connection-type-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-dedicated-vlan-attachment-details-entry-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-interconnect-request-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-interconnect-usage-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-ip-block-entry-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-ip-block-type-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-ip-pool-request-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-ip-provider-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-physical-connection-entry-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-physical-interconnect-link-type-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-session-initialization-mode-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-settings-entry-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-stack-type-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-vlan-attachment-custom-ip-address-example.json
        type: Example
      - url: examples/sase-multitenant-interconnect-api-vlan-attachment-request-example.json
        type: Example
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
      - url: openapi/palo-alto-cloud-identity-engine-api-openapi-original.yml
        type: OpenAPI
      - url: json-schema/cloud-identity-engine-api-attr_based_filter-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-check_group_membership-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-check_user_in_particular_group-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-domain_param-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-fetch_all_users_attrs-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-group_filter-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-list_all_groups_in_domain-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-list_all_users_in_domain-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-list_groups_user_belongs_to-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-list_specific_groups-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-list_specific_users-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-list_users_in_particular_group-schema.json
        type: JSONSchema
      - url: json-schema/cloud-identity-engine-api-pagination_params-schema.json
        type: JSONSchema
      - url: json-structure/cloud-identity-engine-api-attr_based_filter-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-check_group_membership-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-check_user_in_particular_group-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-domain_param-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-fetch_all_users_attrs-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-group_filter-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-list_all_groups_in_domain-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-list_all_users_in_domain-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-list_groups_user_belongs_to-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-list_specific_groups-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-list_specific_users-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-list_users_in_particular_group-structure.json
        type: JSONStructure
      - url: json-structure/cloud-identity-engine-api-pagination_params-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-cloud-identity-engine-api-context.jsonld
        type: JSON-LD
      - url: examples/cloud-identity-engine-api-attr_based_filter-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-check_group_membership-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-check_user_in_particular_group-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-domain_param-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-fetch_all_users_attrs-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-group_filter-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-list_all_groups_in_domain-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-list_all_users_in_domain-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-list_groups_user_belongs_to-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-list_specific_groups-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-list_specific_users-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-list_users_in_particular_group-example.json
        type: Example
      - url: examples/cloud-identity-engine-api-pagination_params-example.json
        type: Example
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
      - url: openapi/palo-alto-prisma-cloud-mssp-api-openapi-original.json
        type: OpenAPI
      - url: json-schema/prisma-cloud-mssp-api-change-password-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-contact-info-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-create-managed-tenant-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-create-mssp-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-create-policy-group-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-create-tenant-group-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-form-login-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-form-login-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-jwk-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-jwks-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-license-info-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-license-pool-info-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-managed-tenant-detailed-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-managed-tenant-license-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-managed-tenant-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-managed-tenants-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-module-info-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-module-info-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-license-info-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-license-pool-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-license-pool-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-license-pools-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-license-usage-request-object-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-license-usage-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-list-user-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-user-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-mssp-user-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-operation-ack-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-operation-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-operations-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-policy-group-info-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-policy-group-list-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-policy-group-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-policy-group-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-policy-groups-list-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-recur-string-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-relative-time-duration-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-relative-time-range-config-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-schedule-task-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-seamless-login-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-stack-mapping-plan-types-list-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-stack-mapping-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-task-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-change-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-group-license-info-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-group-mapping-details-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-group-policy-group-map-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-group-policy-group-mapping-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-group-policy-group-mapping-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-group-policy-group-mappings-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-group-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-groups-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-ids-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-license-usage-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-tenant-update-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-time-range-config-object-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-to-now-time-range-config-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-token-refresh-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-update-managed-tenant-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-update-mssp-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-update-tenant-group-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-v1-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-validate-token-request-schema.json
        type: JSONSchema
      - url: json-schema/prisma-cloud-mssp-api-validate-token-response-schema.json
        type: JSONSchema
      - url: json-structure/prisma-cloud-mssp-api-change-password-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-contact-info-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-create-managed-tenant-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-create-mssp-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-create-policy-group-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-create-tenant-group-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-form-login-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-form-login-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-jwk-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-jwks-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-license-info-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-license-pool-info-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-managed-tenant-detailed-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-managed-tenant-license-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-managed-tenant-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-managed-tenants-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-module-info-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-module-info-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-license-info-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-license-pool-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-license-pool-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-license-pools-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-license-usage-request-object-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-license-usage-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-list-user-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-user-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-mssp-user-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-operation-ack-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-operation-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-operations-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-policy-group-info-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-policy-group-list-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-policy-group-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-policy-group-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-policy-groups-list-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-recur-string-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-relative-time-duration-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-relative-time-range-config-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-schedule-task-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-seamless-login-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-stack-mapping-plan-types-list-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-stack-mapping-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-task-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-change-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-group-license-info-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-group-mapping-details-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-group-policy-group-map-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-group-policy-group-mapping-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-group-policy-group-mapping-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-group-policy-group-mappings-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-group-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-groups-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-ids-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-license-usage-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-tenant-update-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-time-range-config-object-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-to-now-time-range-config-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-token-refresh-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-update-managed-tenant-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-update-mssp-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-update-tenant-group-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-v1-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-validate-token-request-structure.json
        type: JSONStructure
      - url: json-structure/prisma-cloud-mssp-api-validate-token-response-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-cloud-mssp-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-cloud-mssp-api-change-password-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-contact-info-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-create-managed-tenant-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-create-mssp-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-create-policy-group-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-create-tenant-group-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-form-login-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-form-login-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-jwk-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-jwks-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-license-info-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-license-pool-info-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-managed-tenant-detailed-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-managed-tenant-license-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-managed-tenant-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-managed-tenants-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-module-info-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-module-info-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-license-info-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-license-pool-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-license-pool-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-license-pools-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-license-usage-request-object-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-license-usage-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-list-user-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-user-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-mssp-user-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-operation-ack-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-operation-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-operations-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-policy-group-info-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-policy-group-list-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-policy-group-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-policy-group-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-policy-groups-list-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-recur-string-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-relative-time-duration-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-relative-time-range-config-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-schedule-task-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-seamless-login-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-stack-mapping-plan-types-list-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-stack-mapping-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-task-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-change-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-group-license-info-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-group-mapping-details-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-group-policy-group-map-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-group-policy-group-mapping-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-group-policy-group-mapping-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-group-policy-group-mappings-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-group-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-groups-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-ids-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-license-usage-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-tenant-update-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-time-range-config-object-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-to-now-time-range-config-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-token-refresh-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-update-managed-tenant-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-update-mssp-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-update-tenant-group-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-v1-response-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-validate-token-request-example.json
        type: Example
      - url: examples/prisma-cloud-mssp-api-validate-token-response-example.json
        type: Example
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
      - url: json-schema/prisma-access-insights-api-custom-query-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-insights-api-data-resource-query-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-insights-api-data-resource-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-insights-api-export-job-response-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-insights-api-export-job-status-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-insights-api-query-filter-schema.json
        type: JSONSchema
      - url: json-schema/prisma-access-insights-api-time-range-schema.json
        type: JSONSchema
      - url: json-structure/prisma-access-insights-api-custom-query-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-insights-api-data-resource-query-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-insights-api-data-resource-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-insights-api-export-job-response-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-insights-api-export-job-status-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-insights-api-query-filter-structure.json
        type: JSONStructure
      - url: json-structure/prisma-access-insights-api-time-range-structure.json
        type: JSONStructure
      - url: json-ld/palo-alto-prisma-access-insights-api-context.jsonld
        type: JSON-LD
      - url: examples/prisma-access-insights-api-custom-query-example.json
        type: Example
      - url: examples/prisma-access-insights-api-data-resource-query-example.json
        type: Example
      - url: examples/prisma-access-insights-api-data-resource-response-example.json
        type: Example
      - url: examples/prisma-access-insights-api-export-job-response-example.json
        type: Example
      - url: examples/prisma-access-insights-api-export-job-status-example.json
        type: Example
      - url: examples/prisma-access-insights-api-query-filter-example.json
        type: Example
      - url: examples/prisma-access-insights-api-time-range-example.json
        type: Example
    description: A REST API for querying the health and performance of Prisma Access network deployments across multiple API versions (v1.0, v2.0, v3.0). Supports data resource queries for tunnel status, bandwidth utilization, connected user analytics, site health, accelerated application performance, and PAB events. Available for both cloud-managed (TSG-based) and Panorama-managed Prisma Access customers. Uses OAuth 2.0 bearer token authentication consistent with the SASE platform.
common:
  - url: https://pan.dev/
    type: Portal
    description: Central developer hub for all Palo Alto Networks API documentation, SDKs, tutorials, and open-source projects.
  - url: https://docs.paloaltonetworks.com/
    type: Documentation
    description: Palo Alto Networks TechDocs portal with comprehensive product documentation across all platforms and services.
  - url: https://docs.paloaltonetworks.com/develop/api
    type: Documentation
    description: Master API documentation index listing all available APIs across PAN-OS, Prisma Cloud, Cortex, and SASE platforms.
  - url: https://www.paloaltonetworks.com
    type: Website
    description: Palo Alto Networks corporate website with product information, solutions, and company resources.
  - url: https://www.paloaltonetworks.com/services/support
    type: Support
    description: Palo Alto Networks support center for technical assistance, knowledge base, and case management.
  - url: https://www.paloaltonetworks.com/blog/
    type: Blog
    description: Palo Alto Networks blog with cybersecurity research, product updates, and threat intelligence insights.
  - url: https://status.paloaltonetworks.com/
    type: Status
    description: Service status dashboard for Palo Alto Networks cloud services including Prisma Cloud, Cortex, and SASE platforms.
  - url: https://live.paloaltonetworks.com/
    type: Forum
    description: LIVEcommunity forums for peer discussions, knowledge sharing, technical questions, and developer collaboration.
  - url: https://security.paloaltonetworks.com/
    type: Security
    description: Palo Alto Networks PSIRT security advisories portal with vulnerability disclosures and remediation guidance.
  - url: https://github.com/PaloAltoNetworks
    type: GitHubOrganization
    description: Main Palo Alto Networks GitHub organization with 500+ repositories including SDKs, Terraform providers, and automation tools.
  - url: https://github.com/demisto
    type: GitHubOrganization
    description: Cortex XSOAR (formerly Demisto) GitHub organization with open-source integrations, playbooks, and automation content.
  - url: https://github.com/pan-unit42
    type: GitHubOrganization
    description: Unit 42 threat research GitHub organization with threat intelligence tools, IOC feeds, and research publications.
  - url: https://github.com/PaloAltoNetworks/pan-os-python
    type: GitHubRepository
    description: Official Python SDK for PAN-OS firewall and Panorama automation providing an object-oriented interface for configuration management.
  - url: https://github.com/PaloAltoNetworks/pango
    type: GitHubRepository
    description: Official Go SDK for PAN-OS providing the foundation for the Terraform panos provider.
  - url: https://github.com/PaloAltoNetworks/pan-python
    type: GitHubRepository
    description: Low-level Python packages for PAN-OS, WildFire, and AutoFocus providing CLI tools and library modules for XML API, REST API, log collection, and file submission operations.
  - url: https://github.com/PaloAltoNetworks/pan-os-php
    type: GitHubRepository
    description: PHP library for PAN-OS firewall and Panorama configuration management with an object-oriented framework for programmatic rule analysis and policy manipulation.
  - url: https://github.com/PaloAltoNetworks/prisma-sase-sdk-python
    type: SDK
    description: Official Python SDK for Prisma SASE platform APIs including Prisma Access, SD-WAN, and SASE management services.
  - url: https://github.com/PaloAltoNetworks/cortex-cloud-go
    type: SDK
    description: Official Go SDK for Cortex Cloud APIs providing programmatic access to Cortex security operations platform.
  - url: https://github.com/PaloAltoNetworks/cloud-ngfw-aws-go
    type: SDK
    description: Go SDK for Cloud NGFW on AWS providing the underlying library for the Cloud NGFW Terraform provider.
  - url: https://github.com/PaloAltoNetworks/homebrew-cortexcli
    type: CLI
    description: Cortex CLI available via Homebrew and Scoop for command-line interaction with Cortex platform services.
  - url: https://github.com/PaloAltoNetworks/upgrade-assurance-cli
    type: CLI
    description: CLI utility for running PAN-OS upgrade assurance tests to validate firewall readiness before upgrades.
  - url: https://registry.terraform.io/providers/PaloAltoNetworks/panos/latest
    type: TerraformProvider
    description: Terraform provider for PAN-OS enabling infrastructure-as-code management of firewall configuration, security policies, and network objects.
  - url: https://registry.terraform.io/providers/PaloAltoNetworks/scm/latest
    type: TerraformProvider
    description: Terraform provider for Strata Cloud Manager enabling infrastructure-as-code management of unified cloud-based firewall and SASE configuration.
  - url: https://registry.terraform.io/providers/PaloAltoNetworks/cortexcloud/latest
    type: TerraformProvider
    description: Terraform provider for Cortex Cloud enabling infrastructure-as-code management of Cortex security operations platform resources.
  - url: https://registry.terraform.io/providers/PaloAltoNetworks/prismasdwan/latest
    type: TerraformProvider
    description: Terraform provider for Prisma SD-WAN enabling infrastructure-as-code management of SD-WAN sites, policies, and network configuration.
  - url: https://github.com/PaloAltoNetworks/pan-os-upgrade-assurance
    type: Tools
    description: Python library for PAN-OS upgrade assurance providing automated pre and post upgrade checks and network readiness validation.
  - url: https://github.com/PaloAltoNetworks/prisma-cloud-scan
    type: Tools
    description: GitHub Action for scanning container images with Prisma Cloud Compute for vulnerability and compliance checks in CI/CD pipelines.
  - url: https://github.com/PaloAltoNetworks/cobra-tool
    type: Tools
    description: Cloud Offensive Breach and Risk Assessment (COBRA) tool for evaluating cloud security posture and identifying risk exposure.
  - url: https://gallery.pan.dev/
    type: Portal
    description: Palo Alto Networks developer gallery cataloging SDKs, tools, Terraform modules, Ansible collections, and community projects across all product lines.
  - url: https://registry.terraform.io/namespaces/PaloAltoNetworks
    type: TerraformProvider
    description: Palo Alto Networks Terraform providers for PAN-OS, Strata Cloud Manager, Prisma Cloud, and Cloud NGFW infrastructure-as-code.
  - url: https://registry.terraform.io/providers/PaloAltoNetworks/cloudngfwaws/latest
    type: TerraformProvider
    description: Terraform provider for Cloud NGFW on AWS enabling infrastructure-as-code management of cloud-native firewall resources, rule stacks, and security policies.
  - url: https://registry.terraform.io/providers/PaloAltoNetworks/prismacloud/latest
    type: TerraformProvider
    description: Terraform provider for Prisma Cloud enabling infrastructure-as-code management of cloud security policies, compliance standards, alert rules, and cloud account onboarding.
  - url: https://registry.terraform.io/providers/PaloAltoNetworks/prismacloudcompute/latest
    type: TerraformProvider
    description: Terraform provider for Prisma Cloud Compute (CWPP) enabling infrastructure-as-code management of container security policies, runtime rules, and compliance checks.
  - url: https://galaxy.ansible.com/paloaltonetworks/panos
    type: AnsibleCollection
    description: Official Ansible collection for PAN-OS firewall and Panorama automation with 60+ modules for configuration management.
  - url: https://www.paloaltonetworks.com/services/education
    type: Training
    description: Palo Alto Networks education services including training courses, certifications, and digital learning resources.
  - url: https://learn.paloaltonetworks.com
    type: Training
    description: Palo Alto Networks digital learning platform with self-paced courses and certification preparation.
  - url: https://www.paloaltonetworks.com/legal/privacy
    type: PrivacyPolicy
    description: Palo Alto Networks privacy policy detailing data collection, usage, and protection practices.
  - url: https://www.paloaltonetworks.com/legal
    type: TermsOfService
    description: Palo Alto Networks legal terms governing the use of products and services.
  - url: json-ld/palo-alto-networks-security-context.jsonld
    type: JSON-LD
    description: JSON-LD context providing linked data semantics for Palo Alto Networks security data across all product lines including threats, incidents, policies, cloud resources, and AI security scans.
  - url: asyncapi/palo-alto-sase-notifications-asyncapi-original.yml
    type: AsyncAPI
    description: AsyncAPI specification for SASE multitenant notifications including security incidents, platform announcements, dataplane upgrades, and certificate expiry warnings.
  - url: https://x.com/PaloAltoNtwks
    type: X
    description: Palo Alto Networks official account on X with cybersecurity news, product updates, and threat intelligence.
  - url: https://www.youtube.com/@pabornetworks
    type: YouTube
    description: Palo Alto Networks YouTube channel with product demos, tutorials, and cybersecurity webinars.
  - url: https://www.linkedin.com/company/palo-alto-networks
    type: LinkedIn
    description: Palo Alto Networks official LinkedIn page with company updates, cybersecurity insights, and career opportunities.
  - url: https://medium.com/palo-alto-networks-developer-blog
    type: Blog
    description: Palo Alto Networks developer blog on Medium covering API development, DevOps, SecOps, automation, and AI topics.
  - url: https://docs.paloaltonetworks.com/release-notes
    type: ReleaseNotes
    description: Product release notes across all Palo Alto Networks platforms including PAN-OS, Prisma Cloud, Cortex, and SASE products.
  - url: https://pan.dev/sase/docs/release-notes/changelog/
    type: ChangeLog
    description: SASE platform API changelog documenting updates, new endpoints, and breaking changes across Prisma Access, SD-WAN, and SASE management service APIs.
  - url: https://pan.dev/scm/docs/release-notes/changelog/
    type: ChangeLog
    description: Strata Cloud Manager API changelog documenting updates, new features, and changes to the unified cloud management platform API endpoints.
  - url: https://www.postman.com/paloaltonetworks
    type: PostmanWorkspace
    description: Official Palo Alto Networks Postman workspace with API collections for PAN-OS XML API, Cortex XDR, Prisma Cloud, licensing, and cloud services status.
  - url: https://start.paloaltonetworks.com/join-our-slack-community
    type: Slack
    description: Cortex XSOAR DFIR community Slack workspace with over 13,000 members for security automation discussions and integration development support.
  - url: https://unit42.paloaltonetworks.com/
    type: Blog
    description: Unit 42 threat research and intelligence blog with in-depth analysis of malware campaigns, threat actors, vulnerabilities, and emerging cyber threats from Palo Alto Networks threat research team.
  - url: https://cortex.pan.dev/
    type: Portal
    description: Cortex developer documentation portal with API references and guides for Cortex XDR, XSOAR, XSIAM, and Xpanse platforms.
  - url: https://xsoar.pan.dev/
    type: Portal
    description: Cortex XSOAR developer hub with integration development guides, API references, playbook documentation, and automation script resources for the SOAR platform.
  - url: https://pan.dev/swfw/
    type: Documentation
    description: Software Firewall Automation Hub with validated reference architectures and Terraform modules for deploying VM-Series and CN-Series software firewalls in cloud environments.
  - url: https://splunkbase.splunk.com/app/2757
    type: IntegrationsApplication
    description: Splunk App for Palo Alto Networks providing dashboards, reports, and data models for PAN-OS firewall, Panorama, and cloud security log analysis within Splunk.
  - url: https://www.paloaltonetworks.com/partners
    type: Partner
    description: NextWave Partner Program for channel partners, technology partners, and integration developers.
  - type: Features
    data:
      - name: Zero Trust Network Security
        description: Next-generation firewall policies with application, user, and content awareness for enforcing zero trust across on-premises and cloud environments.
      - name: AI-Powered Threat Prevention
        description: Machine learning and deep learning models that detect and prevent known and unknown threats in real time across network traffic, files, and URLs.
      - name: Cloud-Native Application Protection
        description: Full lifecycle cloud security spanning code, build, deploy, and runtime with CSPM, CWPP, code security, and data security posture management.
      - name: Security Orchestration and Automation
        description: Automated incident response with playbooks, integrations, and case management through Cortex XSOAR and XSIAM platforms.
      - name: Extended Detection and Response
        description: Cross-data-source threat detection correlating endpoint, network, cloud, and identity data through Cortex XDR for unified security operations.
      - name: AI Runtime Security
        description: Real-time scanning of AI application prompts and responses for prompt injection, data leakage, toxic content, and other AI-specific threats.
      - name: Secure Access Service Edge
        description: Cloud-delivered security and networking combining Prisma Access, SD-WAN, ZTNA, and cloud SWG for secure access from any location.
      - name: Attack Surface Management
        description: Continuous discovery and monitoring of internet-facing assets and exposures through Cortex Xpanse for external attack surface visibility.
      - name: Infrastructure as Code Security
        description: Automated security scanning of Terraform, CloudFormation, Kubernetes, and other IaC templates for misconfigurations before deployment.
      - name: Digital Experience Monitoring
        description: End-to-end visibility into application performance and user experience across SASE connections with Autonomous DEM.
      - name: Threat Intelligence
        description: Comprehensive threat intelligence through Threat Vault, WildFire malware analysis, DNS Security, and Unit 42 research for proactive defense.
      - name: Multi-Tenant Management
        description: Hierarchical tenant management with delegated administration, aggregate monitoring, and shared policy for MSSPs and large enterprises.
  - type: UseCases
    data:
      - name: SOC Automation
        description: Automate alert triage, incident investigation, and response actions using Cortex XDR, XSOAR playbooks, and XSIAM correlation rules.
      - name: Firewall Policy Management
        description: Programmatically manage security policies, address objects, and NAT rules across PAN-OS firewalls and Panorama using REST or XML APIs.
      - name: Cloud Security Posture
        description: Monitor and remediate cloud misconfigurations, compliance violations, and vulnerabilities across AWS, Azure, and GCP using Prisma Cloud APIs.
      - name: Threat Hunting
        description: Query threat intelligence databases, submit suspicious files for analysis, and correlate IOCs across Threat Vault, WildFire, and DNS Security.
      - name: SASE Deployment Automation
        description: Automate Prisma Access remote network onboarding, SD-WAN site configuration, and ZTNA connector deployment using SASE platform APIs.
      - name: DevSecOps Pipeline Integration
        description: Embed security scanning into CI/CD pipelines with Prisma Cloud code security APIs for IaC scanning, SCA, and secrets detection.
      - name: AI Application Security
        description: Integrate Prisma AIRS API Intercept into AI application code to scan LLM prompts and responses for security threats in real time.
      - name: Compliance Monitoring
        description: Continuously assess cloud infrastructure against CIS benchmarks, PCI DSS, HIPAA, SOC 2, and custom compliance standards using Prisma Cloud.
      - name: Log Forwarding and SIEM Integration
        description: Forward security logs from firewalls and cloud services to Splunk, QRadar, and other SIEMs using Strata Logging Service APIs.
      - name: Multi-Tenant Security Operations
        description: Manage security across tenant hierarchies with aggregate monitoring, shared notifications, and delegated administration for MSSPs.
  - type: Integrations
    data:
      - name: Splunk
        description: Splunk App and Add-on for ingesting PAN-OS, Prisma Cloud, and Cortex logs with pre-built dashboards, reports, and data models.
      - name: Terraform
        description: Official Terraform providers for PAN-OS, Strata Cloud Manager, Prisma Cloud, Cloud NGFW, and Prisma Cloud Compute for infrastructure as code.
      - name: Ansible
        description: Official Ansible collection with 60+ modules for PAN-OS firewall and Panorama configuration automation.
      - name: AWS
        description: Cloud NGFW for AWS, VM-Series on AWS, Prisma Cloud AWS account onboarding, and CloudFormation template support.
      - name: Azure
        description: Cloud NGFW for Azure, VM-Series on Azure, Prisma Cloud Azure subscription onboarding, and Azure AD integration.
      - name: Google Cloud
        description: VM-Series on GCP, Prisma Cloud GCP project onboarding, and Google Workspace integration with Cloud Identity Engine.
      - name: ServiceNow
        description: Cortex XSOAR integration for bi-directional ticket synchronization and automated incident response workflows.
      - name: Slack
        description: Cortex XSOAR Slack integration for alert notifications, war room collaboration, and ChatOps-driven security operations.
      - name: Active Directory
        description: Cloud Identity Engine directory sync with on-premises Active Directory for user-to-IP mapping and identity-aware firewall policies.
      - name: Okta
        description: Cloud Identity Engine integration with Okta for SSO user context and identity-aware security policy enforcement.
  - type: Solutions
    data:
      - name: Strata Network Security Platform
        description: Next-generation firewall platform including PAN-OS hardware and software firewalls, Panorama management, and Strata Cloud Manager.
      - name: Prisma Cloud
        description: Cloud-native application protection platform with CSPM, CWPP, code security, DSPM, and CIEM for multi-cloud environments.
      - name: Prisma SASE
        description: Secure access service edge platform combining Prisma Access, SD-WAN, ZTNA, Autonomous DEM, and cloud SWG.
      - name: Cortex SecOps
        description: Security operations platform with Cortex XDR for detection and response, XSOAR for automation, and XSIAM for AI-driven SOC.
      - name: Prisma AIRS
        description: AI runtime security platform for securing generative AI applications with API Intercept scanning and AI Red Teaming.
      - name: Unit 42 Threat Intelligence
        description: Threat research and intelligence services including Threat Vault, WildFire malware analysis, DNS Security, and security advisory feeds.
  - url: capabilities/incident-response.yaml
    type: NaftikoCapability
    description: Unified incident response capability for SOC analysts combining Cortex XDR, XSIAM, XSOAR, and Xpanse for incident investigation, alert triage, endpoint response, playbook automation, and attack surface assessment with REST and MCP adapters.
  - url: capabilities/threat-intelligence.yaml
    type: NaftikoCapability
    description: Unified threat intelligence capability for threat hunters combining Threat Vault, WildFire, DNS Security, and Security Advisories for IOC research, malware analysis, domain lookups, and vulnerability tracking with REST and MCP adapters.
  - url: capabilities/cloud-security-posture.yaml
    type: NaftikoCapability
    description: Unified cloud security posture capability for cloud security teams combining Prisma Cloud CSPM, Code Security, and DSPM for alert management, policy enforcement, compliance monitoring, code scanning, and data risk assessment with REST and MCP adapters.
  - url: capabilities/network-security-config.yaml
    type: NaftikoCapability
    description: Unified network security configuration capability for firewall admins combining PAN-OS, Strata Cloud Manager, and Cloud NGFW for managing address objects, security rules, NAT rules, rule stacks, and cloud firewalls with REST and MCP adapters.
  - url: capabilities/secure-access.yaml
    type: NaftikoCapability
    description: Unified secure access capability for network engineers combining Prisma Access, ZTNA Connector, SD-WAN, Config Orchestration, and 5G for managing remote networks, zero trust access, SD-WAN sites, and 5G security with REST and MCP adapters.
  - url: capabilities/data-protection.yaml
    type: NaftikoCapability
    description: Unified data protection capability for data security teams combining Enterprise DLP, Email DLP, SaaS Security, and SSPM for managing DLP incidents, email violations, SaaS assets, and posture checks with REST and MCP adapters.
  - url: capabilities/identity-and-access.yaml
    type: NaftikoCapability
    description: Unified identity and access management capability for platform admins combining SASE IAM, Tenancy, and Subscriptions for managing service accounts, access policies, tenant hierarchies, and license allocations with REST and MCP adapters.
  - url: capabilities/monitoring-and-observability.yaml
    type: NaftikoCapability
    description: Unified monitoring and observability capability for operations teams combining Autonomous DEM, Aggregate Monitoring, Strata Logging Service, and AIOps BPA for digital experience tracking, security data aggregation, log forwarding, and best practice assessments with REST and MCP adapters.
  - url: capabilities/ai-security.yaml
    type: NaftikoCapability
    description: Unified AI security capability for AI/ML teams combining Prisma AIRS and AI Red Teaming for scanning AI model inputs and outputs for threats and red-teaming AI applications for vulnerabilities with REST and MCP adapters.
  - url: capabilities/browser-security.yaml
    type: NaftikoCapability
    description: Browser security capability for IT admins wrapping the Prisma Access Browser API for managing enterprise browser policies, user sessions, and deployments with REST and MCP adapters.
  - url: rules/palo-alto-networks-spectral-rules.yml
    type: SpectralRules
    description: Spectral ruleset enforcing API design consistency across all Palo Alto Networks OpenAPI specifications.
  - url: vocabulary/palo-alto-networks-vocabulary.yaml
    type: Vocabulary
    description: Controlled vocabulary of terms and definitions used across Palo Alto Networks API specifications.
  - url: json-ld/palo-alto-networks-context.jsonld
    type: JSON-LD
    description: JSON-LD context providing linked data vocabulary for Palo Alto Networks API entities, properties, and relationships.
---
