---
aid: microsoft-graph
url: https://raw.githubusercontent.com/api-evangelist/microsoft-graph/refs/heads/main/apis.yml
apis:
  - aid: microsoft-graph:microsoft-graph-admin
    name: Microsoft Graph Admin
    tags:
      - Administrative
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/admin?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/admin?view=graph-rest-1.0
        type: Documentation
      - url: openapi/admin-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Admin refers to the administrative capabilities exposed through Microsoft Graph that let IT teams manage and monitor Microsoft 365 from a single, unified API.
  - aid: microsoft-graph:microsoft-graph-agreement-acceptances
    name: Microsoft Graph Agreement Acceptances
    tags:
      - Agreement Acceptances
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/agreementacceptance?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/agreementacceptance?view=graph-rest-1.0
        type: Documentation
      - url: openapi/agreementacceptances-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Agreement Acceptances provides a read-only way to retrieve records of users’ responses to your organization’s Terms of Use configured in Microsoft Entra ID. Each acceptance entry is created automatically when a user (including guests) is prompted and captures who responded, which agreement and file version they saw, their response state (accepted or declined), the timestamp, and—if per‑device consent is required—the device information.
  - aid: microsoft-graph:microsoft-graph-agreements
    name: Microsoft Graph Agreements
    tags:
      - Agreements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/agreement?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/agreement?view=graph-rest-1.0
        type: Documentation
      - url: openapi/agreements-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Agreements is the API for managing Microsoft Entra ID (Azure AD) Terms of Use. It lets organizations programmatically create, publish, localize, and version agreement documents (like EULAs, privacy notices, or acceptable use policies), configure how they’re shown to users, and require acceptance or periodic re-acceptance. Through Conditional Access, you can enforce that users (including guests) must accept terms before signing in or accessing specific apps.
  - aid: microsoft-graph:microsoft-graph-applicaiton-catalogs
    name: Microsoft Graph Applicaiton Catalogs
    tags:
      - Application Catalogs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/teamsapp?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/teamsapp?view=graph-rest-1.0
        type: Documentation
      - url: openapi/appcatalogs-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph App Catalogs is the API surface that lets you programmatically manage Microsoft Teams apps in both the public Teams Store and your organization’s private app catalog. Through the appCatalogs/teamsApps resources, you can discover apps and their versions, retrieve metadata and app definitions, publish and update your own line‑of‑business Teams apps, and remove them when needed.
  - aid: microsoft-graph:microsoft-graph-applications
    name: Microsoft Graph Applications
    tags:
      - Applications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/application?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/application?view=graph-rest-1.0
        type: Documentation
      - url: openapi/applications-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph applications are apps that use the Microsoft Graph API to securely access and orchestrate data across Microsoft 365 and Microsoft Entra ID (Azure AD). Through a single REST endpoint and SDKs, they can read and write mail, calendars, files, users, groups, Teams resources, devices, and security signals, enabling scenarios like workflow automation, user and group lifecycle management, document and calendar integration, insights and analytics, and cross‑app experiences.
  - aid: microsoft-graph:microsoft-graph-application-templates
    name: Microsoft Graph Application Templates
    tags:
      - Application Templates
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/applicationtemplate?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/applicationtemplate?view=graph-rest-1.0
        type: Documentation
      - url: openapi/applicationtemplates-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Application Templates are open‑source, ready‑to‑deploy reference solutions that demonstrate how to build real applications on top of Microsoft Graph and Microsoft 365 data. Each template packages end‑to‑end code (UI, APIs, background processing), Azure infrastructure-as-code, and setup scripts to let you stand up a working solution in minutes.
  - aid: microsoft-graph:microsoft-graph-audit-logs
    name: Microsoft Graph Audit Logs
    tags:
      - Audits
      - Logs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/azure-ad-auditlog-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/azure-ad-auditlog-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/auditlogs-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Audit Logs provide a unified, programmatic way to access and analyze activity and sign-in data from Microsoft Entra ID (Azure Active Directory) and related Microsoft 365 services. Through the Microsoft Graph API, you can query directory audit events (changes to users, groups, apps, roles, policies), user and app sign-in events (including details like time, location, device, conditional access outcome, and risk signals), and provisioning events (account lifecycle actions).
  - aid: microsoft-graph:microsoft-graph-authentication-method-configurations
    name: Microsoft Graph Authentication Method Configurations
    tags:
      - Authentication
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethodconfiguration?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethodconfiguration?view=graph-rest-1.0
        type: Documentation
      - url: openapi/authenticationmethodconfigurations-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Authentication Method Configurations provide programmatic control over which sign-in and multifactor authentication methods are available in Microsoft Entra ID (formerly Azure AD), how they’re configured, and who they apply to.
  - aid: microsoft-graph:microsoft-graph-authentication-methods-policies
    name: Microsoft Graph Authentication Methods Policies
    tags:
      - Authentication
      - Policies
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethodspolicy?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethodspolicy?view=graph-rest-1.0
        type: Documentation
      - url: openapi/authenticationmethodspolicy-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Authentication Methods policies let administrators centrally control which sign-in and verification methods are available in Microsoft Entra ID (Azure AD) and how they’re used.
  - aid: microsoft-graph:microsoft-graph-certificate-based-authorization-configuration
    name: Microsoft Graph Certificate Based Authorization Configuration
    tags:
      - Authorization
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/certificatebasedauthconfiguration?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/certificatebasedauthconfiguration?view=graph-rest-1.0
        type: Documentation
      - url: openapi/certificatebasedauthconfiguration-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph’s certificate-based authentication configuration is a tenant-level setting in Microsoft Entra ID that you manage via the Graph API to enable and govern sign-in using X.509 client certificates. It lets administrators specify which certificate authorities are trusted, how certificate chains and revocation are validated, and how fields in a presented certificate (such as Subject or Subject Alternative Name/UPN) are mapped to a specific user account.
  - aid: microsoft-graph:microsoft-graph-chats
    name: Microsoft Graph Chats
    tags:
      - Chat
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/chat?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/chat?view=graph-rest-1.0
        type: Documentation
      - url: openapi/chats-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Chats is the part of the Microsoft Graph API that lets developers build apps that read, create, and manage Microsoft Teams chats and chat messages. With it, you can list a user’s 1:1, group, and meeting chats; get chat details and members; create new chats; add or remove participants; and send or read messages.
  - aid: microsoft-graph:microsoft-graph-communications
    name: Microsoft Graph Communications
    tags:
      - Communications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/communications-api-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/communications-api-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/communications-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Communications is a set of cloud communications APIs and SDKs in Microsoft Graph that lets developers integrate deeply with Microsoft Teams calling and meetings. It provides endpoints to schedule and manage online meetings, place and control calls (answer, transfer, hold, mute), manage participants, and subscribe to real-time call and meeting events.
  - aid: microsoft-graph:microsoft-graph-compliance
    name: Microsoft Graph Compliance
    tags:
      - Compliance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/complianceapioverview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/complianceapioverview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/compliance-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Compliance is a set of REST APIs that surface Microsoft Purview (Microsoft 365) compliance and privacy capabilities so you can automate workflows across Exchange, SharePoint, OneDrive, and Teams. It lets you orchestrate eDiscovery (Premium) end to end—create cases, add custodians and data sources, place legal holds, run searches, collect to review sets, and export results—integrating these steps into custom apps and processes.
  - aid: microsoft-graph:microsoft-graph-connections
    name: Microsoft Graph Connections
    tags:
      - Connections
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/externalconnectors-externalconnection?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/externalconnectors-externalconnection?view=graph-rest-1.0
        type: Documentation
      - url: openapi/connections-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Connections lets organizations bring external business data—like content from Salesforce, ServiceNow, Confluence, file shares, or custom line‑of‑business apps—into Microsoft 365 by indexing it in Microsoft Graph.
  - aid: microsoft-graph:microsoft-graph-contacts
    name: Microsoft Graph Contacts
    tags:
      - Contacts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/contact?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/contact?view=graph-rest-1.0
        type: Documentation
      - url: openapi/contacts-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Contacts is the part of Microsoft Graph that lets apps access and manage the contacts stored in Microsoft 365 (Outlook) mailboxes through a single REST API. It enables you to list, search, create, update, and delete contacts and contact folders for the signed-in user or other mailboxes you have permission to access, synchronize changes with delta queries, retrieve or update contact photos, and filter/sort results with OData queries.
  - aid: microsoft-graph:microsoft-graph-contracts
    name: Microsoft Graph Contracts
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/contract?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/contract?view=graph-rest-1.0
        type: Documentation
      - url: openapi/contracts-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Contracts is a read-only API in Microsoft Graph that lets Microsoft 365 partners (such as CSP/resellers) discover and list the customer tenants they have a relationship with. It returns each customer’s key directory identifiers and metadata—like tenant (customer) ID, default domain name, display name, and the relationship/contract type—so partner apps can enumerate customers, scope operations per tenant, and obtain tokens targeted at the right directory.
  - aid: microsoft-graph:microsoft-graph-copilot
    name: Microsoft Graph Copilot
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/copilot-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/copilot-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/copilot-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Copilot is an AI assistant that helps developers and IT pros explore and use the Microsoft Graph more easily. You describe what you want in plain language, and it suggests the right Graph APIs, generates REST requests and SDK code snippets, explains required permissions and data models, and helps troubleshoot errors.
  - aid: microsoft-graph:microsoft-graph-data-policy-operations
    name: Microsoft Graph Data Policy Operations
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/datapolicyoperation?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/datapolicyoperation?view=graph-rest-1.0
        type: Documentation
      - url: openapi/datapolicyoperations-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Data Policy Operations is the mechanism Microsoft Graph uses to represent and track long-running, privacy- and compliance-related tasks, most commonly exporting a user’s personal data. When you start an action like exportPersonalData, Graph creates a dataPolicyOperation resource that you can poll to monitor status and progress, inspect errors, and, when finished, obtain the storage location link to download the results.
  - aid: microsoft-graph:microsoft-graph-device-application-management
    name: Microsoft Graph Device Application Management
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-apps-conceptual?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/intune-apps-conceptual?view=graph-rest-1.0
        type: Documentation
      - url: openapi/deviceappmanagement-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Device Application Management is the set of Graph API endpoints that lets you automate Intune app lifecycle tasks across your organization. It enables you to discover, upload, categorize, and assign mobile and Windows apps (including line-of-business and store apps) to user or device groups, apply app configuration policies, and monitor install and update status.
  - aid: microsoft-graph:microsoft-graph-device-management
    name: Microsoft Graph Device Management
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/intune-device-conceptual?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/intune-device-conceptual?view=graph-rest-1.0
        type: Documentation
      - url: openapi/devicemanagement-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Device Management is the set of Microsoft Graph APIs that expose Microsoft Intune’s endpoint management capabilities, letting you automate and integrate device and app lifecycle tasks across Windows, iOS/iPadOS, Android, and macOS. It enables you to inventory devices and apps; create and deploy configuration profiles and compliance policies; assign and manage applications; and perform remote actions such as wipe, retire, restart, sync, reset passcodes, and more.
  - aid: microsoft-graph:microsoft-graph-devices
    name: Microsoft Graph Devices
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/device?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/device?view=graph-rest-1.0
        type: Documentation
      - url: openapi/devices-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Devices refers to the Microsoft Graph APIs that let you discover and manage devices across Azure Active Directory and Microsoft Intune from a single, unified endpoint. Through the /devices resource you can list and query Azure AD–registered or joined devices and their relationships (such as owners and registered users), and via /deviceManagement/managedDevices you can access rich inventory and state for Intune-managed devices, including platform, compliance, and health details.
  - aid: microsoft-graph:microsoft-graph-directory
    name: Microsoft Graph Directory
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
        type: Documentation
      - url: openapi/directory-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Directory is the identity and directory surface of Microsoft Graph, providing programmatic access to an organization’s Microsoft Entra ID (formerly Azure Active Directory). Through a single REST endpoint and SDKs, it lets you read and manage users, groups, devices, applications, roles, domains, administrative units, and directory policies, and navigate their relationships.
  - aid: microsoft-graph:microsoft-graph-directory-objects
    name: Microsoft Graph Directory Objects
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
        type: Documentation
      - url: openapi/directoryobjects-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Directory Objects is the common base resource that represents any identity object stored in Microsoft Entra ID (Azure AD)—including users, groups, devices, service principals, applications, and contacts—and gives them a consistent ID, metadata, and set of relationships.
  - aid: microsoft-graph:microsoft-graph-directory-roles
    name: Microsoft Graph Directory Roles
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
        type: Documentation
      - url: openapi/directoryroles-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Directory Roles provides a REST API to discover, activate, and manage Microsoft Entra ID (formerly Azure Active Directory) directory roles—the RBAC roles that control permissions across Microsoft 365 and Entra. Through the API you can list which roles are active in a tenant, read role definitions from templates, activate built‑in roles, enumerate a role’s members, and add or remove assignments for users, groups, or service principals.
  - aid: microsoft-graph:microsoft-graph-directory-role-templates
    name: Microsoft Graph Directory Role Templates
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
        type: Documentation
      - url: openapi/directoryroletemplates-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph directory role templates are read-only blueprints that represent each built-in Microsoft Entra ID (formerly Azure AD) administrator role, such as Global Administrator or User Administrator. Exposed via the directoryRoleTemplate resource, they let you discover the full set of available roles and their stable template IDs, along with names and descriptions.
  - aid: microsoft-graph:microsoft-graph-domain-dns-records
    name: Microsoft Graph Domain DNS Records
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/domaindnsrecord?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/domaindnsrecord?view=graph-rest-1.0
        type: Documentation
      - url: openapi/domaindnsrecords-openapi-original.yml
        type: OpenAPI
    description: 'Microsoft Graph domain DNS records are the programmatic way to discover and manage the DNS settings Microsoft 365 expects for a custom domain. When you add a domain, Graph exposes two main sets of records: verificationDnsRecords (typically TXT or MX) used to prove ownership, and serviceConfigurationRecords (MX, CNAME, TXT, SRV) used to configure services like Exchange Online (mail flow and Autodiscover), Teams/Skype, and device management.'
  - aid: microsoft-graph:microsoft-graph-domains
    name: Microsoft Graph Domains
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/domain?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/domain?view=graph-rest-1.0
        type: Documentation
      - url: openapi/domains-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Domains is the set of Microsoft Graph APIs and resources for discovering and managing your organization’s domain names in Microsoft Entra ID (Azure AD). It lets you list all domains in a tenant and read key properties (for example, whether a domain is verified, default, initial, root, or which services it supports), add new custom domains, retrieve the DNS records needed for ownership verification, and complete the verification process.
  - aid: microsoft-graph:microsoft-graph-drives
    name: Microsoft Graph Drives
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/drive?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/drive?view=graph-rest-1.0
        type: Documentation
      - url: openapi/drives-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Drives is the part of Microsoft Graph that lets apps discover and work with files across OneDrive and SharePoint using a single, consistent REST API. A drive represents a top-level document library—personal or shared—and exposes its files and folders (driveItems) in the same way whether they live in a user’s OneDrive, a SharePoint site, a Microsoft 365 Group, or a Team.
  - aid: microsoft-graph:microsoft-graph-education
    name: Microsoft Graph Education
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/education-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/education-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/education-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Education is a set of Microsoft Graph APIs that let developers build apps for schools by connecting directly to Microsoft 365 education data and workflows. It exposes structured resources such as schools, classes, teachers, students (educationUser), and supports end-to-end assignment workflows including assignments, submissions, grades, rubrics, and feedback.
  - aid: microsoft-graph:microsoft-graph-employee-experience
    name: Microsoft Graph Employee Experience
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/employee-experience-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/employee-experience-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/employeeexperience-openapi-original.yml
        type: OpenAPI
    description: 'Microsoft Graph Employee Experience is a set of APIs that let developers integrate and extend Microsoft Viva capabilities across Microsoft 365. It focuses especially on learning and growth scenarios: you can connect external learning providers, synchronize course catalogs, create and manage learning assignments, and track users’ course activities—all while honoring Microsoft 365 security, privacy, and consent.'
  - aid: microsoft-graph:microsoft-graph-external
    name: Microsoft Graph External
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/externalconnectors-external?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/externalconnectors-external?view=graph-rest-1.0
        type: Documentation
      - url: openapi/external-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph External is the set of Microsoft Graph capabilities (the /external namespace) that lets you bring content from third‑party apps and line‑of‑business systems into Microsoft 365. You create external connections, define a schema, and push items (with ACLs and properties) so Microsoft indexes them and makes them available in Microsoft Search, Viva, and Copilot alongside native M365 data.
  - aid: microsoft-graph:microsoft-graph-filter-operators
    name: Microsoft Graph Filter Operators
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/filter-query-parameter
    properties:
      - url: https://learn.microsoft.com/en-us/graph/filter-query-parameter
        type: Documentation
      - url: openapi/filteroperators-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph filter operators are the OData $filter expressions you add to Graph API requests to narrow results on the server before they’re returned. They let you select only the resources that match certain criteria—such as equality and comparison checks (eq, ne, gt, ge, lt, le), logical combinations (and, or, not), string matching (startswith, endswith, contains), membership tests (in), and collection predicates (any, all).
  - aid: microsoft-graph:microsoft-graph-functions
    name: Microsoft Graph Functions
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/excel?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/excel?view=graph-rest-1.0
        type: Documentation
      - url: openapi/functions-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Functions is the Excel capability in Microsoft Graph that lets developers invoke hundreds of Excel worksheet functions through REST, running calculations directly on workbooks stored in OneDrive or SharePoint without opening the Excel app.
  - aid: microsoft-graph:microsoft-graph-group-lifecycle-policies
    name: Microsoft Graph Group Lifecycle Policies
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/grouplifecyclepolicy?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/grouplifecyclepolicy?view=graph-rest-1.0
        type: Documentation
      - url: openapi/grouplifecyclepolicies-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Group Lifecycle Policies let administrators govern the lifespan of Microsoft 365 groups by setting an expiration period, scoping the policy to all or selected groups, and automating renewal and cleanup. When a group nears expiration, owners (and optional alternate email recipients) receive reminder emails; if not renewed, the group is soft‑deleted and can be restored within a grace period.
  - aid: microsoft-graph:microsoft-graph-groups
    name: Microsoft Graph Groups
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/groups-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/groups-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/groups-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Groups is the Microsoft Graph API surface for managing Azure AD and Microsoft 365 groups and everything connected to them. It lets you create, read, update, and delete groups; add or remove owners and members (including dynamic membership rules); query transitive membership and changes via delta; and manage group settings and lifecycle policies such as expiration.
  - aid: microsoft-graph:microsoft-graph-group-settings
    name: Microsoft Graph Group Settings
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/groupsetting?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/groupsetting?view=graph-rest-1.0
        type: Documentation
      - url: openapi/groupsettings-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: microsoft-graph:microsoft-graph-group-setting-templates
    name: Microsoft Graph Group Setting Templates
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/groupsettingtemplate?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/groupsettingtemplate?view=graph-rest-1.0
        type: Documentation
      - url: openapi/groupsettingtemplates-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Group Setting Templates are read-only blueprints that define the configurable options you can apply to Microsoft 365 groups (and some other directory objects).
  - aid: microsoft-graph:microsoft-graph-identity
    name: Microsoft Graph Identity
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
        type: Documentation
      - url: openapi/identity-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Identity is the set of Microsoft Graph APIs that expose identity and access capabilities of Microsoft Entra ID (formerly Azure Active Directory) and related services.
  - aid: microsoft-graph:microsoft-graph-identity-governance
    name: Microsoft Graph Identity Governance
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
        type: Documentation
      - url: openapi/identitygovernance-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Identity Governance is the API surface that lets you automate and integrate the identity governance capabilities of Microsoft Entra ID (formerly Azure Active Directory). It helps you enforce least-privilege and zero-trust by controlling and auditing who gets access to what, for how long, and why—across employees, contractors, guests, and connected applications.
  - aid: microsoft-graph:microsoft-graph-identity-protection
    name: Microsoft Graph Identity Protection
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
        type: Documentation
      - url: openapi/identityprotection-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Identity Protection exposes Microsoft Entra ID (formerly Azure AD) Identity Protection signals and controls through the Graph API so you can detect, investigate, and remediate identity risks at scale.
  - aid: microsoft-graph:microsoft-graph-identity-providers
    name: Microsoft Graph Identity Providers
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/identitycontainer?view=graph-rest-1.0
        type: Documentation
      - url: openapi/identityproviders-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Identity Providers is a set of APIs that lets you programmatically manage the sign-in providers your organization offers to customers and guests, primarily for Microsoft Entra External Identities and Azure AD B2C.
  - aid: microsoft-graph:microsoft-graph-information-protection
    name: Microsoft Graph Information Protection
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/informationprotection?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/informationprotection?view=graph-rest-1.0
        type: Documentation
      - url: openapi/informationprotection-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Information Protection is a set of Microsoft Graph APIs that expose Microsoft Purview Information Protection (sensitivity labels and related policies) to applications. It enables developers to discover a tenant’s label taxonomy and policy settings, evaluate which label should apply to given content, and programmatically classify and label files or emails.
  - aid: microsoft-graph:microsoft-graph-invitations
    name: Microsoft Graph Invitations
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/invitation?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/invitation?view=graph-rest-1.0
        type: Documentation
      - url: openapi/invitations-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Invitations is a Microsoft Graph API feature that lets apps programmatically invite external (B2B) users into a Microsoft Entra ID tenant. By calling POST /invitations, it creates a guest user and can send an email invitation with a redemption link, or you can suppress the email and use the returned inviteRedeemUrl to deliver the link yourself.
  - aid: microsoft-graph:microsoft-graph-me
    name: Microsoft Graph Me
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/users?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/users?view=graph-rest-1.0
        type: Documentation
      - url: openapi/me-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph “Me” is a shortcut to the signed-in user’s resource, letting apps work with the current user’s data across Microsoft 365 without knowing their user ID.
  - aid: microsoft-graph:microsoft-graph-oauth2-permission-grants
    name: Microsoft Graph Oauth2 Permission Grants
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/oauth2permissiongrant?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/oauth2permissiongrant?view=graph-rest-1.0
        type: Documentation
      - url: openapi/oauth2permissiongrants-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph OAuth2 Permission Grants (the oAuth2PermissionGrant resource) are the consent records in Microsoft Entra ID that capture which delegated permissions (scopes) a client application’s service principal has to call a resource API on behalf of users.
  - aid: microsoft-graph:microsoft-graph-organizations
    name: Microsoft Graph Organizations
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/organization?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/organization?view=graph-rest-1.0
        type: Documentation
      - url: openapi/organization-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Organizations exposes a tenant’s organization profile in Microsoft Entra ID (formerly Azure Active Directory) so apps can discover and manage directory‑level information through a single API.
  - aid: microsoft-graph:microsoft-graph-permission-grants
    name: Microsoft Graph Permission Grants
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/resourcespecificpermissiongrant?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/resourcespecificpermissiongrant?view=graph-rest-1.0
        type: Documentation
      - url: openapi/permissiongrants-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph permission grants are the records and APIs in Microsoft Entra ID that represent the consent an application has to access resources. They link a client app (service principal) to a resource API and the specific permissions approved, and are used during token issuance to determine what the app can do.
  - aid: microsoft-graph:microsoft-graph-places
    name: Microsoft Graph Places
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/place?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/place?view=graph-rest-1.0
        type: Documentation
      - url: openapi/places-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Places is an API surface in Microsoft Graph that lets applications discover and work with physical location resources in Microsoft 365—primarily meeting rooms and room lists (and, in some tenants, workspaces). It provides a tenant-wide, directory-backed catalog of places that apps can list and query, returning rich metadata such as name, address, coordinates, building and floor details, email address, and capacity.
  - aid: microsoft-graph:microsoft-graph-planner
    name: Microsoft Graph Planner
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/planner-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Planner is the set of Microsoft Graph APIs that lets developers programmatically work with Microsoft Planner data across Microsoft 365. With it, you can create and manage plans, buckets, and tasks; assign tasks to people; set due dates, priority, progress, labels, checklists, and attachments; and move tasks across boards to reflect workflow.
  - aid: microsoft-graph:microsoft-graph-policies
    name: Microsoft Graph Policies
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/policy-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/policy-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/policies-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Policies is the set of Microsoft Graph API endpoints that let administrators and developers read and manage tenant-wide policy settings across Microsoft Entra ID and Microsoft 365.
  - aid: microsoft-graph:microsoft-graph-print
    name: Microsoft Graph Print
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/print?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/print?view=graph-rest-1.0
        type: Documentation
      - url: openapi/print-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Print (the Universal Print APIs in Microsoft Graph) lets developers integrate secure, cloud-based printing into their apps and workflows. Through these APIs, you can discover and register organization printers, manage printer shares and access, submit and spool print jobs (including uploading documents), set print options, and monitor job and device status. It also supports automation via print tasks and subscriptions for event-driven processing and notifications.
  - aid: microsoft-graph:microsoft-graph-privacy
    name: Microsoft Graph Privacy
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/privacy?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/privacy?view=graph-rest-1.0
        type: Documentation
      - url: openapi/privacy-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: microsoft-graph:microsoft-graph-reports
    name: Microsoft Graph Reports
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/report?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/report?view=graph-rest-1.0
        type: Documentation
      - url: openapi/reports-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Reports is the reporting surface of Microsoft 365 exposed via Microsoft Graph, enabling administrators to programmatically retrieve usage, adoption, and certain identity and print analytics across their tenant.
  - aid: microsoft-graph:microsoft-graph-role-management
    name: Microsoft Graph Role Management
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/rolemanagement?view=graph-rest-1.0
        type: Documentation
      - url: openapi/rolemanagement-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Role Management provides a unified API to programmatically manage role-based access across Microsoft Entra ID (Azure AD) and supported services like Microsoft 365 and Intune. It lets you list and inspect built-in and custom role definitions, create or update custom roles, and assign roles to users, groups, or service principals at tenant-wide or resource-scoped levels.
  - aid: microsoft-graph:microsoft-graph-schema-extensions
    name: Microsoft Graph Schema Extensions
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/schemaextension?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/schemaextension?view=graph-rest-1.0
        type: Documentation
      - url: openapi/schemaextensions-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph schema extensions let you add your own strongly typed fields to Microsoft 365 resources—such as users, groups, messages, events, devices, and more—so your application’s data can live alongside Microsoft data and be accessed through the same Graph APIs.
  - aid: microsoft-graph:microsoft-graph-scoped-role-memberships
    name: Microsoft Graph Scoped Role Memberships
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/scopedrolemembership?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/scopedrolemembership?view=graph-rest-1.0
        type: Documentation
      - url: openapi/scopedrolememberships-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Scoped Role Memberships let you programmatically assign and manage Azure AD (Microsoft Entra ID) directory roles with a limited scope to an administrative unit, rather than tenant-wide. Exposed through the scopedRoleMembership resource, these assignments delegate administrative permissions (for example, User Administrator or Helpdesk Administrator) so that the assignee’s authority applies only to the users, groups, or other objects contained in a specific administrative unit.
  - aid: microsoft-graph:microsoft-graph-search
    name: Microsoft Graph Search
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/search-api-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/search-api-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/search-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Search is the unified enterprise search capability for Microsoft 365, exposed via the Microsoft Graph API, that lets apps query and discover content across services like SharePoint, OneDrive, Outlook, Teams, and more—as well as external systems connected through Graph connectors. It returns security‑trimmed, relevance‑ranked, and personalized results based on the user’s permissions and work signals.
  - aid: microsoft-graph:microsoft-graph-security
    name: Microsoft Graph Security
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/security-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Security is a unified set of APIs within Microsoft Graph that lets you access, correlate, and act on security data across Microsoft 365 and integrated security solutions. It normalizes alerts and incidents from Microsoft Defender products and other providers, exposes security posture information such as Secure Score, and supports managing threat intelligence indicators.
  - aid: microsoft-graph:microsoft-graph-service-principals
    name: Microsoft Graph Service Principals
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/serviceprincipal?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/serviceprincipal?view=graph-rest-1.0
        type: Documentation
      - url: openapi/serviceprincipals-openapi-original.yml
        type: OpenAPI
    description: In Microsoft Entra ID (formerly Azure AD), a service principal is the identity an application uses to access resources, and the Microsoft Graph service principal is the tenant-local representation of the Microsoft Graph API itself. It publishes the set of OAuth 2.0 delegated scopes and application roles (permissions) that apps can request, and it is the target against which your app’s own service principal is granted consent.
  - aid: microsoft-graph:microsoft-graph-shares
    name: Microsoft Graph Shares
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/shares?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/shares?view=graph-rest-1.0
        type: Documentation
      - url: openapi/shares-openapi-original.yml
        type: OpenAPI
    description: 'Microsoft Graph Shares is the part of Microsoft Graph that lets apps access a OneDrive or SharePoint item by its sharing link or token, without needing to know the site, drive, or item IDs. Given a share URL, you can resolve it to a sharedDriveItem and then work with the underlying driveItem or listItem: read metadata, navigate folder children, fetch thumbnails, and download content—and, if the link grants edit rights, make changes.'
  - aid: microsoft-graph:microsoft-graph-sites
    name: Microsoft Graph Sites
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0
        type: Documentation
      - url: openapi/sites-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Sites is the Graph API surface for SharePoint Online, letting apps discover and work with sites and their content through a single, secure endpoint. It enables you to locate the root site or a site by URL, search for sites, and navigate a site’s structure to access document libraries (drives), lists, list items, files, and modern site pages.
  - aid: microsoft-graph:microsoft-graph-solutions
    name: Microsoft Graph Solutions
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/solutions-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/solutions-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/solutions-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph solutions connect apps to the data and intelligence across Microsoft 365 through a single, unified API. They enable secure access to users, groups, mail, calendars, files, Teams chats and meetings, SharePoint, OneDrive, Planner, devices, and security signals, so you can build experiences that personalize collaboration, automate workflows, and derive insights.
  - aid: microsoft-graph:microsoft-graph-storage
    name: Microsoft Graph Storage
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/filestorage?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/filestorage?view=graph-rest-1.0
        type: Documentation
      - url: openapi/storage-openapi-original.yml
        type: OpenAPI
    description: “Microsoft Graph storage” typically refers to the storage capabilities exposed through Microsoft Graph—primarily OneDrive and SharePoint—via the Files and Drives APIs. It lets apps programmatically store and manage files and folders, upload and download (including large-file upload sessions), track changes with delta queries, generate thumbnails, search, and share content with rich permission controls.
  - aid: microsoft-graph:microsoft-graph-subscribed-skus
    name: Microsoft Graph Subscribed SKUs
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/subscribedsku?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/subscribedsku?view=graph-rest-1.0
        type: Documentation
      - url: openapi/subscribedskus-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Subscribed SKUs is the API/resource that lists the Microsoft 365/Azure AD license subscriptions your tenant owns. When you call GET /subscribedSkus, it returns each license plan (SKU) with its identifiers (skuId, skuPartNumber), seat counts (prepaidUnits and consumedUnits), subscription status (enabled, suspended, warning), and the included service plans.
  - aid: microsoft-graph:microsoft-graph-subscriptions
    name: Microsoft Graph Subscriptions
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/subscription?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/subscription?view=graph-rest-1.0
        type: Documentation
      - url: openapi/subscriptions-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Subscriptions let your app receive near real-time change notifications (webhooks) when Microsoft 365 data changes—such as Outlook mail and calendar items, users and groups, files in OneDrive/SharePoint, or Teams chats and channels. You register a subscription that specifies the resource to watch and a publicly reachable HTTPS endpoint; Microsoft Graph validates the endpoint and then posts notifications whenever relevant items are created, updated, or deleted.
  - aid: microsoft-graph:microsoft-graph-teams
    name: Microsoft Graph Teams
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/teams-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph for Teams exposes Microsoft Teams data and capabilities through a single, secure API so you can build integrations and automate Teams at scale. With it, you can create and manage teams, channels, chats, and memberships; post and read messages; schedule and manage meetings and webinars; access presence and call records; and install or configure Teams apps and tabs.
  - aid: microsoft-graph:microsoft-graph-teams-templates
    name: Microsoft Graph Teams Templates
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0
        type: Documentation
      - url: openapi/teamstemplates-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: microsoft-graph:microsoft-graph-teamwork
    name: Microsoft Graph Teamwork
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/teamwork?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/teamwork?view=graph-rest-1.0
        type: Documentation
      - url: openapi/teamwork-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Teamwork is the set of Microsoft Graph APIs that surface Microsoft Teams collaboration capabilities. It lets you programmatically create and manage teams and channels; add members and owners; read, post, and moderate chat and channel messages; install, configure, and manage Teams apps and tabs; work with frontline workforce features like schedules, shifts, and time off; use teamwork tags to target groups; send activity notifications; and discover a user’s associated teams.
  - aid: microsoft-graph:microsoft-graph-tenant-relationships
    name: Microsoft Graph Tenant Relationships
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/tenantrelationship?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/tenantrelationship?view=graph-rest-1.0
        type: Documentation
      - url: openapi/tenantrelationships-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Tenant Relationships is the part of the Microsoft Graph API that lets you model and manage how your Microsoft Entra ID tenant relates to other tenants. It provides endpoints to discover external tenants, create and govern delegated admin relationships (GDAP) between partners and customers, manage membership in a multi-tenant organization, and access “managed tenants” data used by Microsoft 365 Lighthouse.
  - aid: microsoft-graph:microsoft-graph-users
    name: Microsoft Graph Users
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0
        type: Documentation
      - url: openapi/users-openapi-original.yml
        type: OpenAPI
    description: Microsoft Graph Users refers to the Users resource in Microsoft Graph, which exposes Microsoft Entra ID (Azure AD) user accounts and their relationships and Microsoft 365 data through a unified API. It lets you list, read, create, update, and delete users; manage identities and lifecycle tasks such as assigning licenses, resetting passwords, and updating authentication settings; and retrieve related information like profile details, photos, managers, direct reports, group and role memberships.
  - aid: microsoft-graph:token
    name: Token
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
      - type: OpenAPI
        url: properties/token-openapi-original.yml
  - aid: microsoft-graph:workspaces
    name: Workspaces
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/workplace?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/workplace?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/workspaces-openapi-original.yml
  - aid: microsoft-graph:sites
    name: Sites
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/sites-openapi-original.yml
  - aid: microsoft-graph:collections
    name: Collections
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/collections-openapi-original.yml
  - aid: microsoft-graph:pages
    name: Pages
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/sitepage?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/sitepage?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/pages-openapi-original.yml
  - aid: microsoft-graph:assets
    name: Assets
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/assets-openapi-original.yml
  - aid: microsoft-graph:asset-folders
    name: Asset Folders
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/asset-folders-openapi-original.yml
  - aid: microsoft-graph:webhooks
    name: Webhooks
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/subscription?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/subscription?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/webhooks-openapi-original.yml
  - aid: microsoft-graph:forms
    name: Forms
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/forms-openapi-original.yml
  - aid: microsoft-graph:form-submissions
    name: Form Submissions
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/form-submissions-openapi-original.yml
  - aid: microsoft-graph:token
    name: Token
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
      - type: OpenAPI
        url: properties/token-openapi-original.yml
  - aid: microsoft-graph:workspaces
    name: Workspaces
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/workplace?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/workplace?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/workspaces-openapi-original.yml
  - aid: microsoft-graph:sites
    name: Sites
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/sites-openapi-original.yml
  - aid: microsoft-graph:collections
    name: Collections
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/collections-openapi-original.yml
  - aid: microsoft-graph:pages
    name: Pages
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/sitepage?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/sitepage?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/pages-openapi-original.yml
  - aid: microsoft-graph:assets
    name: Assets
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/assets-openapi-original.yml
  - aid: microsoft-graph:asset-folders
    name: Asset Folders
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/asset-folders-openapi-original.yml
  - aid: microsoft-graph:webhooks
    name: Webhooks
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/subscription?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/subscription?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/webhooks-openapi-original.yml
  - aid: microsoft-graph:forms
    name: Forms
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/forms-openapi-original.yml
  - aid: microsoft-graph:form-submissions
    name: Form Submissions
    description: Needs a description.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags: []
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: properties/form-submissions-openapi-original.yml
name: Microsoft Graph
tags:
  - Azure AD
  - Collaboration
  - Contacts
  - Documents
  - Email
  - Graph
  - Identity
  - Microsoft
  - Office 365
  - Presentations
  - Productivity
  - Spreadsheets
  - T1
  - Tasks
type: Index
image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
access: 3rd-Party
common:
  - url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    name: Portal
    type: Portal
  - url: https://developer.microsoft.com/en-us/graph/changelog/?showfilters=false
    name: Change Log
    type: ChangeLog
  - url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview?context=graph%2Fapi%2F1.0&view=graph-rest-1.0
    name: SDKs
    type: SDKs
  - url: https://learn.microsoft.com/en-us/graph/versioning-and-support?view=graph-rest-1.0
    name: Versioning
    type: Versioning
  - url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use?context=graph%2Fcontext&view=graph-rest-1.0
    name: Terms Of Service
    type: TermsOfService
  - url: https://learn.microsoft.com/en-us/graph/graph-explorer/graph-explorer-overview?view=graph-rest-1.0
    name: Getting Started
    type: GettingStarted
  - url: https://developer.microsoft.com/en-us/graph/graph-explorer
    name: Explorer
    type: Explorer
  - url: openapi/v1.0
    name: OpenAPI
    type: OpenAPI
  - url: https://developer.microsoft.com/en-us/graph/blogs/
    type: Blog
  - url: https://github.com/microsoftgraph
    type: GitHub Organization
  - url: https://stackoverflow.com/questions/tagged/microsoft-graph
    type: Stack Overflow
  - url: https://techcommunity.microsoft.com/t5/microsoft-365-developer-platform/ct-p/Microsoft365DeveloperPlatform
    type: Community
  - url: https://developer.microsoft.com/en-us/graph/status
    type: Status
  - url: https://docs.microsoft.com/en-us/graph/samples
    type: Samples
  - url: https://docs.microsoft.com/en-us/graph/throttling
    type: Rate Limits
  - url: https://docs.microsoft.com/en-us/graph/best-practices-concept
    type: Best Practices
  - url: https://learn.microsoft.com/en-us/graph/overview
    type: Documentation
  - url: https://learn.microsoft.com/en-us/graph/auth/
    type: Authentication
  - url: https://learn.microsoft.com/en-us/graph/permissions-reference
    type: Permissions
  - url: https://learn.microsoft.com/en-us/graph/tutorials/
    type: Tutorials
  - url: https://developer.microsoft.com/en-us/graph/quick-start
    type: QuickStart
  - url: https://learn.microsoft.com/en-us/graph/errors
    type: Errors
  - url: https://developer.microsoft.com/en-us/graph/support
    type: Support
  - url: https://learn.microsoft.com/en-us/graph/whats-new-overview
    type: ChangeLog
    name: What Is New
  - url: https://learn.microsoft.com/en-us/graph/use-the-api
    type: GettingStarted
    name: Use The API
  - url: https://learn.microsoft.com/en-us/training/paths/m365-msgraph-fundamentals/
    type: Training
  - url: https://learn.microsoft.com/en-us/graph/metered-api-overview
    type: Pricing
  - url: https://learn.microsoft.com/en-us/answers/tags/161/ms-graph
    type: Forum
  - url: https://privacy.microsoft.com/en-us/privacystatement
    type: Privacy Policy
  - url: https://www.microsoft.com
    type: Website
  - url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
    type: Sign Up
  - url: https://developer.microsoft.com/en-us/graph
    type: Login
  - url: https://learn.microsoft.com/en-us/graph/use-postman
    type: PostmanCollection
  - url: https://www.youtube.com/@Microsoft365Developer
    type: YouTube
  - url: https://github.com/microsoftgraph/microsoft-graph-docs-contrib/issues
    type: Issue Tracker
  - url: https://learn.microsoft.com/en-us/graph/sdks/sdk-installation
    type: Client Libraries
  - url: https://learn.microsoft.com/en-us/graph/security-overview
    type: Security
created: '2025-08-20'
modified: '2026-04-28'
position: Consumer
description: Microsoft Graph is the gateway to data and intelligence in Microsoft 365. It provides a unified programmability model that you can use to access data in Microsoft 365, Windows 10, and Enterprise Mobility + Security.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Microsoft
    email: graphsdkpub@microsoft.com
    url: https://developer.microsoft.com/en-us/graph
specificationVersion: '0.19'
---
