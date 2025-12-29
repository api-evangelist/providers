---
aid: microsoft-graph
url: >-
  https://raw.githubusercontent.com/api-evangelist/microsoft-graph/refs/heads/main/apis.yml
apis:
  - aid: microsoft-graph:microsoft-graph-admin
    name: Microsoft Graph Admin
    tags:
      - Administrative
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/admin-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Admin refers to the administrative capabilities exposed
      through Microsoft Graph that let IT teams manage and monitor Microsoft 365
      from a single, unified API. It enables you to provision and govern
      identities and access (users, groups, roles, licenses) in Microsoft Entra
      ID; manage devices and apps with Intune; configure and operate
      collaboration services like Teams, SharePoint, and Exchange; pull audit,
      usage, and security insights; and monitor service health and Message
      Center communications. With granular, consent-based permissions plus
      features like delta queries and webhooks, it supports automation of
      lifecycle tasks, policy enforcement at scale, reporting and analytics, and
      integration with CI/CD and ITSM workflows.
  - aid: microsoft-graph:microsoft-graph-agreement-acceptances
    name: Microsoft Graph Agreement Acceptances
    tags:
      - Agreement Acceptances
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/agreementacceptances-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Agreement Acceptances provides a read-only way to retrieve
      records of users responses to your organizations Terms of Use configured
      in Microsoft Entra ID. Each acceptance entry is created automatically when
      a user (including guests) is prompted and captures who responded, which
      agreement and file version they saw, their response state (accepted or
      declined), the timestamp, andif perdevice consent is requiredthe device
      information. Through Microsoft Graph you can list and filter these records
      (for example by userId or agreementId) to build compliance and audit
      reports, verify who accepted which terms and when, and integrate this
      evidence into governance, automation, or SIEM workflows.
  - aid: microsoft-graph:microsoft-graph-agreements
    name: Microsoft Graph Agreements
    tags:
      - Agreements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/agreements-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Agreements is the API for managing Microsoft Entra ID
      (Azure AD) Terms of Use. It lets organizations programmatically create,
      publish, localize, and version agreement documents (like EULAs, privacy
      notices, or acceptable use policies), configure how theyre shown to
      users, and require acceptance or periodic re-acceptance. Through
      Conditional Access, you can enforce that users (including guests) must
      accept terms before signing in or accessing specific apps. The API also
      provides detailed acceptance recordswho accepted, when, which version,
      and often device/contextso you can audit compliance at scale and automate
      workflows around policy updates.
  - aid: microsoft-graph:microsoft-graph-applicaiton-catalogs
    name: Microsoft Graph Applicaiton Catalogs
    tags:
      - Application Catalogs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/appcatalogs-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph App Catalogs is the API surface that lets you
      programmatically manage Microsoft Teams apps in both the public Teams
      Store and your organizations private app catalog. Through the
      appCatalogs/teamsApps resources, you can discover apps and their versions,
      retrieve metadata and app definitions, publish and update your own
      lineofbusiness Teams apps, and remove them when needed. It also supports
      installing or removing apps for users, teams, or group chats at scale,
      enabling endtoend automation of app lifecycle and governance from within
      your tenant. Access is controlled by Graph permissions (for example,
      AppCatalog.Read.All or AppCatalog.ReadWrite.All), so admins can integrate
      approval, rollout, and maintenance workflows into their existing tooling.
  - aid: microsoft-graph:microsoft-graph-applications
    name: Microsoft Graph Applications
    tags:
      - Applications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/applications-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph applications are apps that use the Microsoft Graph API to
      securely access and orchestrate data across Microsoft 365 and Microsoft
      Entra ID (Azure AD). Through a single REST endpoint and SDKs, they can
      read and write mail, calendars, files, users, groups, Teams resources,
      devices, and security signals, enabling scenarios like workflow
      automation, user and group lifecycle management, document and calendar
      integration, insights and analytics, and crossapp experiences. They
      support both delegated permissions (acting as a signedin user) and
      application permissions (daemon/background services), along with webhooks
      for change notifications, batching, and advanced query capabilities.
      Developers can build web, mobile, desktop, and server apps that connect to
      Outlook, OneDrive, SharePoint, Teams, Planner, Excel, and moreusing
      Microsoft identity, consent, and scopes to enforce finegrained,
      enterprisegrade security.
  - aid: microsoft-graph:microsoft-graph-application-templates
    name: Microsoft Graph Application Templates
    tags:
      - Application Templates
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/applicationtemplates-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Application Templates are opensource, readytodeploy
      reference solutions that demonstrate how to build real applications on top
      of Microsoft Graph and Microsoft 365 data. Each template packages
      endtoend code (UI, APIs, background processing), Azure
      infrastructure-as-code, and setup scripts to let you stand up a working
      solution in minutes. They showcase best practices for authentication and
      consent, app registration, permission models (delegated and application),
      webhooks and notifications, incremental sync, and use of common Microsoft
      Graph workloads like users, groups, mail, calendar, files, and Teams.
      Teams can use them to learn proven patterns, accelerate development, or
      customize them into production apps while benefiting from security,
      governance, and deployment guidance.
  - aid: microsoft-graph:microsoft-graph-audit-logs
    name: Microsoft Graph Audit Logs
    tags:
      - Audits
      - Logs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/auditlogs-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Audit Logs provide a unified, programmatic way to access
      and analyze activity and sign-in data from Microsoft Entra ID (Azure
      Active Directory) and related Microsoft 365 services. Through the
      Microsoft Graph API, you can query directory audit events (changes to
      users, groups, apps, roles, policies), user and app sign-in events
      (including details like time, location, device, conditional access
      outcome, and risk signals), and provisioning events (account lifecycle
      actions). This enables security monitoring, incident investigation,
      compliance reporting, and operational troubleshooting, with support for
      filtering, sorting, and time-bound queries. Retention periods and
      available fields depend on your tenants licensing and configuration, and
      the data can be exported or integrated into SIEM and automation workflows.
  - aid: microsoft-graph:microsoft-graph-authentication-method-configurations
    name: Microsoft Graph Authentication Method Configurations
    tags:
      - Authentication
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/authenticationmethodconfigurations-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Authentication Method Configurations provide programmatic
      control over which sign-in and multifactor authentication methods are
      available in Microsoft Entra ID (formerly Azure AD), how theyre
      configured, and who they apply to. Through Graph endpointssuch as the
      authentication methods policy and method-specific resourcesyou can enable
      or disable options like Microsoft Authenticator, FIDO2 security keys,
      Temporary Access Pass, SMS/voice, email OTP (for guests), and
      certificate-based authentication; target them to specific users or groups;
      require registration; and fine-tune settings (for example, number
      matching, passwordless mode, key restrictions, or allowed device types).
      This enables automation and consistency across environments, supports
      DevOps-style change management, and helps enforce a strong, auditable
      identity security posture at scale.
  - aid: microsoft-graph:microsoft-graph-authentication-methods-policies
    name: Microsoft Graph Authentication Methods Policies
    tags:
      - Authentication
      - Policies
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/authenticationmethodspolicy-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Authentication Methods policies let administrators
      centrally control which sign-in and verification methods are available in
      Microsoft Entra ID (Azure AD) and how theyre used. Through Graph API
      endpoints, you can enable or disable specific methods (for example
      Microsoft Authenticator, FIDO2/passkeys, Temporary Access Pass,
      SMS/voice), target them to selected users or groups, and configure
      behavior such as registration requirements, use for MFA and selfservice
      password reset, key and device restrictions, TAP lifetimes/onetime use,
      and features like number matching for Authenticator. These policies
      support automation at scale, integrate with Conditional Access and
      authentication strengths to enforce required factors, and provide a
      consistent way to govern and standardize authentication across your
      tenant.
  - aid: >-
      microsoft-graph:microsoft-graph-certificate-based-authorization-configuration
    name: Microsoft Graph Certificate Based Authorization Configuration
    tags:
      - Authorization
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/certificatebasedauthconfiguration-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graphs certificate-based authentication configuration is a
      tenant-level setting in Microsoft Entra ID that you manage via the Graph
      API to enable and govern sign-in using X.509 client certificates. It lets
      administrators specify which certificate authorities are trusted, how
      certificate chains and revocation are validated, and how fields in a
      presented certificate (such as Subject or Subject Alternative Name/UPN)
      are mapped to a specific user account. During sign-in, Entra ID uses this
      configuration to validate the certificate, bind it to the right identity,
      and issue tokens for Microsoft Graph and other apps, allowing
      organizations to automate and control certificate-based sign-in without
      relying on AD FS.
  - aid: microsoft-graph:microsoft-graph-chats
    name: Microsoft Graph Chats
    tags:
      - Chat
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/chats-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Chats is the part of the Microsoft Graph API that lets
      developers build apps that read, create, and manage Microsoft Teams chats
      and chat messages. With it, you can list a users 1:1, group, and meeting
      chats; get chat details and members; create new chats; add or remove
      participants; and send or read messages. It supports rich message features
      like mentions, reactions, formatting, and file attachments, and you can
      install apps or tabs into a chat and subscribe to change notifications to
      react to new messages in near real time. Access is controlled through
      Microsoft Graph permissions (for example, Chat.Read, Chat.ReadWrite, and
      ChatMember.ReadWrite) in delegated or application contexts, subject to
      tenant policies and admin consent.
  - aid: microsoft-graph:microsoft-graph-communications
    name: Microsoft Graph Communications
    tags:
      - Communications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/communications-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Communications is a set of cloud communications APIs and
      SDKs in Microsoft Graph that lets developers integrate deeply with
      Microsoft Teams calling and meetings. It provides endpoints to schedule
      and manage online meetings, place and control calls (answer, transfer,
      hold, mute), manage participants, and subscribe to real-time call and
      meeting events. Using the real-time media platform and SDKs, you can build
      voice/video botssuch as IVRs, meeting assistants, and compliance
      recording solutionsthat join Teams calls and meetings (including those
      with PSTN participants) to process or capture media. It also exposes call
      records and quality metrics for post-call analytics and troubleshooting.
      All of this is delivered through the unified Graph endpoint with Azure
      AD-based authentication and tenant- or user-scoped permissions.
  - aid: microsoft-graph:microsoft-graph-compliance
    name: Microsoft Graph Compliance
    tags:
      - Compliance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/compliance-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Compliance is a set of REST APIs that surface Microsoft
      Purview (Microsoft 365) compliance and privacy capabilities so you can
      automate workflows across Exchange, SharePoint, OneDrive, and Teams. It
      lets you orchestrate eDiscovery (Premium) end to endcreate cases, add
      custodians and data sources, place legal holds, run searches, collect to
      review sets, and export resultsintegrating these steps into custom apps
      and processes. It also provides programmatic access to information
      protection and data classification features such as working with
      sensitivity labels, and supports managing subject rights requests to meet
      privacy regulations. Built on Microsoft Graphs permissions, RBAC, and
      auditing, the APIs enable secure, scalable compliance solutions that align
      with your existing Microsoft Purview configurations.
  - aid: microsoft-graph:microsoft-graph-connections
    name: Microsoft Graph Connections
    tags:
      - Connections
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/connections-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Connections lets organizations bring external business
      datalike content from Salesforce, ServiceNow, Confluence, file shares, or
      custom lineofbusiness appsinto Microsoft 365 by indexing it in
      Microsoft Graph. Through prebuilt or custom connectors and ingestion APIs,
      it normalizes items, schemas, and permissions so that the content is
      securitytrimmed and searchable across Microsoft Search, appears in apps
      like SharePoint, Outlook, and Teams, and can be used by Copilot for
      Microsoft 365 to ground its responses. Admins configure connections in the
      Microsoft 365 admin center, manage indexing and access controls, and
      benefit from Microsoft 365 compliance and governance features applied to
      the external data.
  - aid: microsoft-graph:microsoft-graph-contacts
    name: Microsoft Graph Contacts
    tags:
      - Contacts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/contacts-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Contacts is the part of Microsoft Graph that lets apps
      access and manage the contacts stored in Microsoft 365 (Outlook) mailboxes
      through a single REST API. It enables you to list, search, create, update,
      and delete contacts and contact folders for the signed-in user or other
      mailboxes you have permission to access, synchronize changes with delta
      queries, retrieve or update contact photos, and filter/sort results with
      OData queries. With delegated and application permissions controlled by
      Microsoft identity, it supports personal, shared, and delegated scenarios,
      making it easy to keep address books in sync and integrate contact data
      across Microsoft 365 services and devices.
  - aid: microsoft-graph:microsoft-graph-contracts
    name: Microsoft Graph Contracts
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/contracts-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Contracts is a read-only API in Microsoft Graph that lets
      Microsoft 365 partners (such as CSP/resellers) discover and list the
      customer tenants they have a relationship with. It returns each customers
      key directory identifiers and metadatalike tenant (customer) ID, default
      domain name, display name, and the relationship/contract typeso partner
      apps can enumerate customers, scope operations per tenant, and obtain
      tokens targeted at the right directory. The relationship itself is
      established and managed in Partner Center (not via the API). For newer,
      granular delegated admin scenarios, partners typically also use the
      tenantRelationships/delegatedAdminRelationships APIs alongside Contracts.
  - aid: microsoft-graph:microsoft-graph-copilot
    name: Microsoft Graph Copilot
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/copilot-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Copilot is an AI assistant that helps developers and IT
      pros explore and use the Microsoft Graph more easily. You describe what
      you want in plain language, and it suggests the right Graph APIs,
      generates REST requests and SDK code snippets, explains required
      permissions and data models, and helps troubleshoot errors. In tools like
      Graph Explorer and developer workflows, it can run sample or tenant-scoped
      queries, inspect responses, and propose follow-up queries or
      documentation, speeding up tasks such as integrating mail, calendar,
      users, Teams, and files into apps or building Copilot extensions that use
      Microsoft 365 data. It honors your organizations security and only works
      with data youre authorized to access.
  - aid: microsoft-graph:microsoft-graph-data-policy-operations
    name: Microsoft Graph Data Policy Operations
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/datapolicyoperations-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Data Policy Operations is the mechanism Microsoft Graph
      uses to represent and track long-running, privacy- and compliance-related
      tasks, most commonly exporting a users personal data. When you start an
      action like exportPersonalData, Graph creates a dataPolicyOperation
      resource that you can poll to monitor status and progress, inspect errors,
      and, when finished, obtain the storage location link to download the
      results. You can also list operations across the tenant to monitor and
      audit requests. This enables organizations to automate subject-rights
      workflows (such as GDPR/CCPA data export) across Microsoft 365 services
      through a consistent, asynchronous API.
  - aid: microsoft-graph:microsoft-graph-device-application-management
    name: Microsoft Graph Device Application Management
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/deviceappmanagement-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Device Application Management is the set of Graph API
      endpoints that lets you automate Intune app lifecycle tasks across your
      organization. It enables you to discover, upload, categorize, and assign
      mobile and Windows apps (including line-of-business and store apps) to
      user or device groups, apply app configuration policies, and monitor
      install and update status. It also supports mobile application management
      without device enrollment by creating and targeting app protection
      policies for iOS and Android, tracking managed app registrations and
      status, and managing Windows Information Protection policies. Beyond apps,
      it provides capabilities to manage Apple VPP/Apple Business Manager tokens
      and licenses, distribute managed eBooks, maintain enterprise code-signing
      certificates, and run app management tasks. With appropriate permissions
      (for example, DeviceManagementApps.ReadWrite.All and
      DeviceManagementManagedApps.ReadWrite), it enables end-to-end automation
      and integration with CI/CD and reporting workflows.
  - aid: microsoft-graph:microsoft-graph-device-management
    name: Microsoft Graph Device Management
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/devicemanagement-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Device Management is the set of Microsoft Graph APIs that
      expose Microsoft Intunes endpoint management capabilities, letting you
      automate and integrate device and app lifecycle tasks across Windows,
      iOS/iPadOS, Android, and macOS. It enables you to inventory devices and
      apps; create and deploy configuration profiles and compliance policies;
      assign and manage applications; and perform remote actions such as wipe,
      retire, restart, sync, reset passcodes, and more. You can manage
      enrollments (including Windows Autopilot and Apple Automated Device
      Enrollment), apply role-based access and scope tags, and retrieve rich
      reports, audit logs, and analytics on device health and compliance.
      Because its part of Microsoft Graph, you can combine device management
      with identity, security, and productivity data to build end-to-end
      automation and insights.
  - aid: microsoft-graph:microsoft-graph-devices
    name: Microsoft Graph Devices
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/devices-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Devices refers to the Microsoft Graph APIs that let you
      discover and manage devices across Azure Active Directory and Microsoft
      Intune from a single, unified endpoint. Through the /devices resource you
      can list and query Azure ADregistered or joined devices and their
      relationships (such as owners and registered users), and via
      /deviceManagement/managedDevices you can access rich inventory and state
      for Intune-managed devices, including platform, compliance, and health
      details. Beyond inventory, the Intune endpoints enable lifecycle and
      support actionssuch as sync, retire, wipe, restart, remote lock, and
      moresubject to the appropriate permissions and device platform
      capabilities. Organizations use these APIs to build asset inventories,
      drive conditional access and app targeting, automate helpdesk workflows,
      and integrate device context into security and compliance processes across
      Windows, iOS/iPadOS, macOS, and Android.
  - aid: microsoft-graph:microsoft-graph-directory
    name: Microsoft Graph Directory
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/directory-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Directory is the identity and directory surface of
      Microsoft Graph, providing programmatic access to an organizations
      Microsoft Entra ID (formerly Azure Active Directory). Through a single
      REST endpoint and SDKs, it lets you read and manage users, groups,
      devices, applications, roles, domains, administrative units, and directory
      policies, and navigate their relationships. It enables common scenarios
      like user provisioning and deprovisioning, group membership and licensing,
      app registration and consent, device inventory, access governance, and
      compliance reporting. The API supports rich capabilities such as OData
      queries, delta change tracking, batching, and change notifications, all
      governed by Graphs granular permission model for delegated and app-only
      access. Because its part of Microsoft Graph, directory objects are
      seamlessly connected to Microsoft 365 services (like Teams, SharePoint,
      Outlook, and security), making it easier to build identity-aware apps and
      automated workflows across the tenant.
  - aid: microsoft-graph:microsoft-graph-directory-objects
    name: Microsoft Graph Directory Objects
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/directoryobjects-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Directory Objects is the common base resource that
      represents any identity object stored in Microsoft Entra ID (Azure
      AD)including users, groups, devices, service principals, applications,
      and contactsand gives them a consistent ID, metadata, and set of
      relationships. Through this type and its child resources, apps can list
      and read objects, search and filter, paginate results, and traverse
      relationships such as memberOf, transitive memberships, owners,
      createdObjects, and ownedObjects. It also provides helper methods for
      directory intelligence and lifecycle tasks, such as delta queries to track
      changes, getByIds to resolve mixed sets of IDs, membership checks
      (checkMemberGroups/Objects, getMemberGroups/Objects, isMemberOf), and
      restore to recover soft-deleted items. Reference operations let you add or
      remove members and owners, enabling scenarios like access governance,
      entitlement management, and authorization. All access is enforced via
      Microsoft Graph permissions (for example, Directory.Read.All or
      Directory.ReadWrite.All) and respects directory policies and controls.
  - aid: microsoft-graph:microsoft-graph-directory-roles
    name: Microsoft Graph Directory Roles
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/directoryroles-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Directory Roles provides a REST API to discover, activate,
      and manage Microsoft Entra ID (formerly Azure Active Directory) directory
      rolesthe RBAC roles that control permissions across Microsoft 365 and
      Entra. Through the API you can list which roles are active in a tenant,
      read role definitions from templates, activate builtin roles, enumerate a
      roles members, and add or remove assignments for users, groups, or
      service principals. It also supports change tracking (delta queries) to
      monitor role membership over time. This enables organizations to automate
      leastprivilege access, inventory and audit who has what permissions, and
      integrate role governance into provisioning and compliance workflows.
  - aid: microsoft-graph:microsoft-graph-directory-role-templates
    name: Microsoft Graph Directory Role Templates
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/directoryroletemplates-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph directory role templates are read-only blueprints that
      represent each built-in Microsoft Entra ID (formerly Azure AD)
      administrator role, such as Global Administrator or User Administrator.
      Exposed via the directoryRoleTemplate resource, they let you discover the
      full set of available roles and their stable template IDs, along with
      names and descriptions. You can use a templates ID to activate that role
      in your tenant by creating a directoryRole (POST to /directoryRoles with
      the roleTemplateId), after which the role appears in the directoryRoles
      collection and can have members assigned. Templates themselves cant be
      modified or assigned; they exist to enumerate built-in roles and enable
      consistent, automated activation across tenants.
  - aid: microsoft-graph:microsoft-graph-domain-dns-records
    name: Microsoft Graph Domain DNS Records
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/domaindnsrecords-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph domain DNS records are the programmatic way to discover
      and manage the DNS settings Microsoft 365 expects for a custom domain.
      When you add a domain, Graph exposes two main sets of records:
      verificationDnsRecords (typically TXT or MX) used to prove ownership, and
      serviceConfigurationRecords (MX, CNAME, TXT, SRV) used to configure
      services like Exchange Online (mail flow and Autodiscover), Teams/Skype,
      and device management. Each record is typed (for example
      DomainDnsTxtRecord, DomainDnsCnameRecord, DomainDnsMxRecord,
      DomainDnsSrvRecord) and includes details such as host name, target, and
      TTL. Apps can read these records to guide admins, automate onboarding,
      monitor when verification can succeed, and then invoke the domain verify
      action. Graph itself doesnt change your DNS; you publish the returned
      records at your DNS host, and Graph reflects their status for Microsoft
      365 setup and health checks.
  - aid: microsoft-graph:microsoft-graph-domains
    name: Microsoft Graph Domains
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/domains-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Domains is the set of Microsoft Graph APIs and resources
      for discovering and managing your organizations domain names in Microsoft
      Entra ID (Azure AD). It lets you list all domains in a tenant and read key
      properties (for example, whether a domain is verified, default, initial,
      root, or which services it supports), add new custom domains, retrieve the
      DNS records needed for ownership verification, and complete the
      verification process. You can also manage authentication settings (managed
      or federated), work with federation configurations for SSO, and delete
      domains when theyre no longer referenced. These capabilities enable
      automation for tenant provisioning, domain onboarding and migration, and
      consistent domain governance across Microsoft 365 services.
  - aid: microsoft-graph:microsoft-graph-drives
    name: Microsoft Graph Drives
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/drives-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Drives is the part of Microsoft Graph that lets apps
      discover and work with files across OneDrive and SharePoint using a
      single, consistent REST API. A drive represents a top-level document
      librarypersonal or sharedand exposes its files and folders (driveItems)
      in the same way whether they live in a users OneDrive, a SharePoint site,
      a Microsoft 365 Group, or a Team. With it, you can list and search items,
      read and write file metadata and content, upload large files via upload
      sessions, move/copy/rename, manage versions, generate sharing links, and
      control permissions. It supports change tracking with delta queries and
      subscriptions (webhooks), plus thumbnails, previews, and special folders
      like root and Documents. Drives are addressed with endpoints such as
      /me/drive, /users/{id}/drive, /sites/{id}/drive, and /drives/{id}, with
      access governed by Microsoft Entra (Azure AD) scopes like Files.Read or
      Sites.Read.All. In short, it provides a unified, permission-aware way to
      build file-centric experiences across Microsoft 365.
  - aid: microsoft-graph:microsoft-graph-education
    name: Microsoft Graph Education
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/education-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Education is a set of Microsoft Graph APIs that let
      developers build apps for schools by connecting directly to Microsoft 365
      education data and workflows. It exposes structured resources such as
      schools, classes, teachers, students (educationUser), and supports
      end-to-end assignment workflows including assignments, submissions,
      grades, rubrics, and feedback. With it, apps can create and manage class
      rosters, automate assignment distribution and collection, track progress
      and grading, and integrate with Teams for Education, OneNote Class
      Notebooks, files, and calendars. It also includes School Data Sync (SDS)
      capabilities to provision and synchronize rosters from student information
      systems. Because it runs on Microsoft Graph, it uses the same security,
      permissions, and compliance model as the rest of Microsoft 365, enabling
      secure, permissioned access and scalable integrations across the education
      ecosystem.
  - aid: microsoft-graph:microsoft-graph-employee-experience
    name: Microsoft Graph Employee Experience
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/employeeexperience-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Employee Experience is a set of APIs that let developers
      integrate and extend Microsoft Viva capabilities across Microsoft 365. It
      focuses especially on learning and growth scenarios: you can connect
      external learning providers, synchronize course catalogs, create and
      manage learning assignments, and track users course activitiesall while
      honoring Microsoft 365 security, privacy, and consent. By exposing
      resources such as learning providers, course activities, and assignments,
      the APIs make it easy to automate training workflows, surface personalized
      learning inside Teams and other apps, and build custom dashboards that
      help organizations improve engagement, upskilling, and overall employee
      experience.
  - aid: microsoft-graph:microsoft-graph-external
    name: Microsoft Graph External
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/external-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph External is the set of Microsoft Graph capabilities (the
      /external namespace) that lets you bring content from thirdparty apps and
      lineofbusiness systems into Microsoft 365. You create external
      connections, define a schema, and push items (with ACLs and properties) so
      Microsoft indexes them and makes them available in Microsoft Search, Viva,
      and Copilot alongside native M365 data. It supports security trimming,
      incremental updates and deletions, activity signals, and querying via the
      Graph search API, and you can use prebuilt connectors or build custom
      ingestion with the API.
  - aid: microsoft-graph:microsoft-graph-filter-operators
    name: Microsoft Graph Filter Operators
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/filteroperators-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph filter operators are the OData $filter expressions you add
      to Graph API requests to narrow results on the server before theyre
      returned. They let you select only the resources that match certain
      criteriasuch as equality and comparison checks (eq, ne, gt, ge, lt, le),
      logical combinations (and, or, not), string matching (startswith,
      endswith, contains), membership tests (in), and collection predicates
      (any, all). Using filters reduces payload size and improves performance by
      avoiding clientside postprocessing. Support for specific operators
      varies by resource and property (not all fields are filterable), and some
      advanced scenarioslike filtering on certain directory properties or using
      $count with filtersrequire the ConsistencyLevel: eventual header.
  - aid: microsoft-graph:microsoft-graph-functions
    name: Microsoft Graph Functions
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/functions-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Functions is the Excel capability in Microsoft Graph that
      lets developers invoke hundreds of Excel worksheet functions through REST,
      running calculations directly on workbooks stored in OneDrive or
      SharePoint without opening the Excel app. Your app calls the
      workbook/functions endpoints with parameters (for example SUM, XLOOKUP,
      FILTER, DATE, financial and statistical functions), and the service
      returns typed results that can be written back to cells or used to drive
      business logic. Because the calculations execute server-side within a
      workbook session, you can automate analytics, validations, and
      transformations at scale, combine them with tables, ranges, and charts
      APIs, and orchestrate end-to-end Excel workflows via Graph.
  - aid: microsoft-graph:microsoft-graph-group-lifecycle-policies
    name: Microsoft Graph Group Lifecycle Policies
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/grouplifecyclepolicies-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Group Lifecycle Policies let administrators govern the
      lifespan of Microsoft 365 groups by setting an expiration period, scoping
      the policy to all or selected groups, and automating renewal and cleanup.
      When a group nears expiration, owners (and optional alternate email
      recipients) receive reminder emails; if not renewed, the group is
      softdeleted and can be restored within a grace period. Policies can be
      created and managed programmatically via Microsoft Graphspecifying the
      lifetime in days, choosing which groups are managed, adding or removing
      groups from a policy, and triggering renewalshelping organizations reduce
      stale groups, maintain directory hygiene, and enforce consistent
      governance at scale.
  - aid: microsoft-graph:microsoft-graph-groups
    name: Microsoft Graph Groups
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/groups-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Groups is the Microsoft Graph API surface for managing
      Azure AD and Microsoft 365 groups and everything connected to them. It
      lets you create, read, update, and delete groups; add or remove owners and
      members (including dynamic membership rules); query transitive membership
      and changes via delta; and manage group settings and lifecycle policies
      such as expiration. For Microsoft 365 groups, it also links to the groups
      collaborative assetsSharePoint site and files (drive), mailbox and
      calendar, Planner plans, and Microsoft Teamsso apps can provision groups,
      automate membership and governance, and enable endtoend collaboration
      scenarios. It supports change notifications/webhooks and enables
      group-based access control, licensing, and app role assignments to
      centralize permissions and compliance.
  - aid: microsoft-graph:microsoft-graph-group-settings
    name: Microsoft Graph Group Settings
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/groupsettings-openapi-original.yml
        type: OpenAPI
    description: Needs a description
  - aid: microsoft-graph:microsoft-graph-group-setting-templates
    name: Microsoft Graph Group Setting Templates
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/groupsettingtemplates-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Group Setting Templates are read-only blueprints that
      define the configurable options you can apply to Microsoft 365 groups (and
      some other directory objects). Administrators use these templates (for
      example, those covering naming policies, guest access, classifications,
      welcome emails, and usage-guidelines URLs) to create directory settings
      that enforce organizationwide or pergroup behaviorsuch as who can
      create groups, whether guests are allowed, or what classifications are
      available. The templates provide the schema and validation for each
      setting, ensuring consistent and predictable configuration through the
      Graph API and the Entra admin portal. In practice, you query the available
      templates (GET /groupSettingTemplates), then instantiate one as a
      directory setting with your values (POST /groupSettings) and apply it at
      the tenant or group scope; the templates themselves remain immutable.
  - aid: microsoft-graph:microsoft-graph-identity
    name: Microsoft Graph Identity
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/identity-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Identity is the set of Microsoft Graph APIs that expose
      identity and access capabilities of Microsoft Entra ID (formerly Azure
      Active Directory) and related services. Through a single REST endpoint and
      SDKs, it lets developers and admins manage users, groups, devices,
      applications and service principals; assign roles and permissions;
      configure authentication methods (MFA, passwordless) and conditional
      access; and orchestrate identity lifecycle and governance (provisioning,
      access packages, access reviews, entitlement management). It also surfaces
      security and compliance signalssuch as sign-in and audit logs and risk
      detectionsfor monitoring and response. Organizations use it to build SSO
      experiences, automate provisioning and access, enforce least privilege,
      support B2B/B2C collaboration, and integrate identity with broader
      Microsoft 365 data and workflows.
  - aid: microsoft-graph:microsoft-graph-identity-governance
    name: Microsoft Graph Identity Governance
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/identitygovernance-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Identity Governance is the API surface that lets you
      automate and integrate the identity governance capabilities of Microsoft
      Entra ID (formerly Azure Active Directory). It helps you enforce
      least-privilege and zero-trust by controlling and auditing who gets access
      to what, for how long, and whyacross employees, contractors, guests, and
      connected applications. Through Graph, you can orchestrate
      joinermoverleaver lifecycle workflows; deliver governed access via
      entitlement management (catalogs, access packages, and approval policies);
      run one-time and recurring access reviews and app consent reviews; publish
      and track terms-of-use acceptance; and manage privileged access with
      just-in-time elevation through Privileged Identity Management for roles
      and groups. These APIs support external users, policy and
      separation-of-duties constraints, and provide rich auditing and reporting
      so you can embed governance into custom apps and automated processes at
      scale.
  - aid: microsoft-graph:microsoft-graph-identity-protection
    name: Microsoft Graph Identity Protection
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/identityprotection-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Identity Protection exposes Microsoft Entra ID (formerly
      Azure AD) Identity Protection signals and controls through the Graph API
      so you can detect, investigate, and remediate identity risks at scale. It
      provides programmatic access to risk detections and risk levels for users,
      sign-ins, and service principals; surfaces indicators such as leaked
      credentials, unfamiliar sign-in properties, impossible travel,
      malware-linked or anonymous IPs, password spray, and token theft; and
      preserves risk history. Using the API, you can list and filter risky
      entities, confirm compromise or dismiss false positives, trigger
      remediation (for example, require password reset or MFA via risk-based
      policies), and manage Identity Protection policies to automate response.
      This enables integration with SIEM/SOAR and custom apps to monitor,
      triage, and enforce risk-based conditional access across your tenant.
  - aid: microsoft-graph:microsoft-graph-identity-providers
    name: Microsoft Graph Identity Providers
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/identityproviders-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Identity Providers is a set of APIs that lets you
      programmatically manage the sign-in providers your organization offers to
      customers and guests, primarily for Microsoft Entra External Identities
      and Azure AD B2C. With it, you can create, configure, list, and delete
      identity providers such as Microsoft account, Google, Facebook, Apple,
      built-in methods like email one-time passcode, and OpenID
      Connectcompliant providers; supply client IDs/secrets and issuer/metadata
      endpoints; and attach those providers to B2C user flows or custom policies
      so apps can present the right sign-in options. This enables consistent,
      automated setup across environments and gives you centralized control over
      how users authenticate and which accounts are accepted.
  - aid: microsoft-graph:microsoft-graph-information-protection
    name: Microsoft Graph Information Protection
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/informationprotection-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Information Protection is a set of Microsoft Graph APIs
      that expose Microsoft Purview Information Protection (sensitivity labels
      and related policies) to applications. It enables developers to discover a
      tenants label taxonomy and policy settings, evaluate which label should
      apply to given content, and programmatically classify and label files or
      emails. Apps can read, apply, update, or remove sensitivity labels and
      inspect the protection settings those labels enforce, such as encryption
      and usage rights. These capabilities let organizations automate labeling
      workflows, embed labeling into custom solutions, run whatif policy
      evaluations, and keep protection and governance consistent across
      Microsoft 365 services like Office apps, SharePoint, OneDrive, and
      Exchange.
  - aid: microsoft-graph:microsoft-graph-invitations
    name: Microsoft Graph Invitations
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/invitations-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Invitations is a Microsoft Graph API feature that lets
      apps programmatically invite external (B2B) users into a Microsoft Entra
      ID tenant. By calling POST /invitations, it creates a guest user and can
      send an email invitation with a redemption link, or you can suppress the
      email and use the returned inviteRedeemUrl to deliver the link yourself.
      You can set the invited users email and display name, choose a
      post-acceptance redirect URL (often a deep link to your app), and
      customize the invitation message and recipients. When the invite is
      redeemed, the user is added as a guest (userType=Guest) and can be
      assigned to apps, groups, and resources per your policies. This enables
      automated, governed cross-tenant collaboration and streamlined external
      user onboarding.
  - aid: microsoft-graph:microsoft-graph-me
    name: Microsoft Graph Me
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/me-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Me is a shortcut to the signed-in users resource,
      letting apps work with the current users data across Microsoft 365
      without knowing their user ID. Through the /me endpoint, you can retrieve
      and update profile details and settings; get the users photo and
      presence; read, send, and organize mail; manage calendar events and
      contacts; access OneDrive files; interact with Teams chats and joined
      teams; view manager, direct reports, and group memberships; and work with
      To Do and Planner tasks. All operations are governed by OAuth permissions
      and tenant policies, so apps only see or change what the user or admin has
      consented to.
  - aid: microsoft-graph:microsoft-graph-oauth2-permission-grants
    name: Microsoft Graph Oauth2 Permission Grants
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/oauth2permissiongrants-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph OAuth2 Permission Grants (the oAuth2PermissionGrant
      resource) are the consent records in Microsoft Entra ID that capture which
      delegated permissions (scopes) a client applications service principal
      has to call a resource API on behalf of users. Each grant ties the client
      service principal to the resource service principal, indicates whether the
      consent is per-user (Principal) or tenant-wide via admin consent
      (AllPrincipals), and stores the space-delimited scopes and optional
      validity period. During token issuance, Entra ID relies on these grants to
      decide whether to issue an access token with the requested scopes;
      removing a grant prevents future tokens for those scopes and forces
      re-consent. Admins and automation use Microsoft Graph to list, audit,
      create, update, or revoke these grants to enforce least privilege and
      govern app access. Note that oAuth2PermissionGrant covers delegated
      permissions only; application permissions are represented separately by
      app role assignments (appRoleAssignment). These objects dont contain
      tokens or secretsthey are authoritative consent records used by the
      authorization system.
  - aid: microsoft-graph:microsoft-graph-organizations
    name: Microsoft Graph Organizations
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/organization-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Organizations exposes a tenants organization profile in
      Microsoft Entra ID (formerly Azure Active Directory) so apps can discover
      and manage directorylevel information through a single API. It lets you
      read core details like the tenants display name and ID, verified domains,
      and service/plan state, and access related resources such as
      organizational branding and privacy/contact settings; you can also update
      certain tenant-wide settings (for example, branding and notification
      contacts) with the right permissions. Typical uses include tailoring
      multitenant app experiences, verifying domain ownership, showing company
      details in app UIs, checking which Microsoft 365 services are available,
      and automating compliance or branding at the tenant level.
  - aid: microsoft-graph:microsoft-graph-permission-grants
    name: Microsoft Graph Permission Grants
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/permissiongrants-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph permission grants are the records and APIs in Microsoft
      Entra ID that represent the consent an application has to access
      resources. They link a client app (service principal) to a resource API
      and the specific permissions approved, and are used during token issuance
      to determine what the app can do. There are two main forms: delegated
      permission grants (oAuth2PermissionGrant), which capture user-consented
      scopes or tenant-wide admin consent, and app role assignments, which
      capture application permissions for app-only access. Using Microsoft
      Graph, administrators can list, audit, create, and revoke these grants to
      manage app access, respond to risk, and enforce least-privilege practices.
      In short, permission grants operationalize consent by making it
      inspectable and controllable across the tenant.
  - aid: microsoft-graph:microsoft-graph-places
    name: Microsoft Graph Places
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/places-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Places is an API surface in Microsoft Graph that lets
      applications discover and work with physical location resources in
      Microsoft 365primarily meeting rooms and room lists (and, in some
      tenants, workspaces). It provides a tenant-wide, directory-backed catalog
      of places that apps can list and query, returning rich metadata such as
      name, address, coordinates, building and floor details, email address, and
      capacity. Developers use it to power room-finder and location-aware
      experiences: searching and filtering places by attributes, showing details
      to users, and combining results with calendar endpoints to check
      availability and schedule meetings. Access is secured via Microsoft Graph
      permissions (for example, Place.Read.All), and supports operations to list
      places, get a specific place, and update certain properties.
  - aid: microsoft-graph:microsoft-graph-planner
    name: Microsoft Graph Planner
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/planner-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Planner is the set of Microsoft Graph APIs that lets
      developers programmatically work with Microsoft Planner data across
      Microsoft 365. With it, you can create and manage plans, buckets, and
      tasks; assign tasks to people; set due dates, priority, progress, labels,
      checklists, and attachments; and move tasks across boards to reflect
      workflow. It supports both group-based plans and roster-based plans, so
      you can manage membership and access whether a plan is tied to a Microsoft
      365 group or a lightweight roster. The APIs enable automation and
      integration scenariossuch as syncing tasks with line-of-business systems,
      building dashboards and reports, or triggering workflows and
      notificationswhile honoring Microsoft 365 permissions and compliance.
      Theyre available via REST and Microsoft Graph SDKs with delegated or
      application permissions.
  - aid: microsoft-graph:microsoft-graph-policies
    name: Microsoft Graph Policies
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/policies-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Policies is the set of Microsoft Graph API endpoints that
      let administrators and developers read and manage tenant-wide policy
      settings across Microsoft Entra ID and Microsoft 365. Through a single,
      programmable interface, you can automate and enforce organization-wide
      rules for things like authentication methods and strengths (including MFA
      registration), authorization and session behavior, admin consent workflows
      and permission grant policies, application management restrictions,
      cross-tenant access and B2B trust, role management/PIM settings, feature
      rollouts, and home realm discovery. Using these APIs enables consistent
      security, compliance, and collaboration controls at scale, integrates
      policy changes into automation and CI/CD, and provides centralized
      governance that applies across Microsoft cloud services.
  - aid: microsoft-graph:microsoft-graph-print
    name: Microsoft Graph Print
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/print-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Print (the Universal Print APIs in Microsoft Graph) lets
      developers integrate secure, cloud-based printing into their apps and
      workflows. Through these APIs, you can discover and register organization
      printers, manage printer shares and access, submit and spool print jobs
      (including uploading documents), set print options, and monitor job and
      device status. It also supports automation via print tasks and
      subscriptions for event-driven processing and notifications. Because its
      built on Microsoft 365 and Azure AD, it uses role-based access and can
      route jobs to cloud-managed or connector-attached on-premises
      printerseliminating the need for local print servers or device-specific
      drivers.
  - aid: microsoft-graph:microsoft-graph-privacy
    name: Microsoft Graph Privacy
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/privacy-openapi-original.yml
        type: OpenAPI
    description: Needs a description
  - aid: microsoft-graph:microsoft-graph-reports
    name: Microsoft Graph Reports
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/reports-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Reports is the reporting surface of Microsoft 365 exposed
      via Microsoft Graph, enabling administrators to programmatically retrieve
      usage, adoption, and certain identity and print analytics across their
      tenant. Through the /reports endpoints, you can pull tenant- and
      user-level metrics for services like Teams, SharePoint, OneDrive,
      Exchange, Yammer/Viva Engage, Microsoft 365 Apps, and Universal
      Printcovering activity (active users, messages, meetings, file actions),
      storage and mailbox usage, app activations, and device usageas well as
      Azure AD registration and MFA usage details. Reports are available for
      defined periods (for example, the last 7, 30, 90, or 180 days) and can be
      exported for automation and BI workflows, typically as CSV and, for some
      endpoints, as JSON. With the appropriate permissions (such as
      Reports.Read.All), you can schedule extractions, integrate them with other
      Graph data, and build dashboards to track adoption, capacity, and trends.
  - aid: microsoft-graph:microsoft-graph-role-management
    name: Microsoft Graph Role Management
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/rolemanagement-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Role Management provides a unified API to programmatically
      manage role-based access across Microsoft Entra ID (Azure AD) and
      supported services like Microsoft 365 and Intune. It lets you list and
      inspect built-in and custom role definitions, create or update custom
      roles, and assign roles to users, groups, or service principals at
      tenant-wide or resource-scoped levels. The APIs also integrate with
      Privileged Identity Management (PIM) for just-in-time access, enabling
      eligibility, time-bound assignments, approvals, activation, and auditing.
      With these endpoints, you can automate least-privilege governancediscover
      who has which permissions, manage lifecycle changes to roles and
      assignments, and embed RBAC operations into provisioning and compliance
      workflows.
  - aid: microsoft-graph:microsoft-graph-schema-extensions
    name: Microsoft Graph Schema Extensions
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/schemaextensions-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph schema extensions let you add your own strongly typed
      fields to Microsoft 365 resourcessuch as users, groups, messages, events,
      devices, and moreso your applications data can live alongside Microsoft
      data and be accessed through the same Graph APIs. You register a schema
      extension (with a unique ID tied to your verified domain), define property
      names and types, and then write values to individual resource instances;
      those values are returned with the resource and can be selected or, on
      supported entities, filtered in queries. Unlike untyped open extensions,
      schema extensions are discoverable and enforce types, making them easier
      to share across apps and tenants and to manage through a defined
      lifecycle. This approach reduces the need for a separate store or custom
      service, keeps data consistent and secured under Microsoft Graphs auth
      model, and enables richer, domain-specific solutions built on top of
      Microsoft 365.
  - aid: microsoft-graph:microsoft-graph-scoped-role-memberships
    name: Microsoft Graph Scoped Role Memberships
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/scopedrolememberships-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Scoped Role Memberships let you programmatically assign
      and manage Azure AD (Microsoft Entra ID) directory roles with a limited
      scope to an administrative unit, rather than tenant-wide. Exposed through
      the scopedRoleMembership resource, these assignments delegate
      administrative permissions (for example, User Administrator or Helpdesk
      Administrator) so that the assignees authority applies only to the users,
      groups, or other objects contained in a specific administrative unit. This
      enables leastprivilege, regional or departmental delegation, supports
      listing and removing scoped assignments, and provides a way to audit who
      has which admin capabilities over which subset of the directoryall via
      Microsoft Graph.
  - aid: microsoft-graph:microsoft-graph-search
    name: Microsoft Graph Search
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/search-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Search is the unified enterprise search capability for
      Microsoft 365, exposed via the Microsoft Graph API, that lets apps query
      and discover content across services like SharePoint, OneDrive, Outlook,
      Teams, and moreas well as external systems connected through Graph
      connectors. It returns securitytrimmed, relevanceranked, and
      personalized results based on the users permissions and work signals.
      Developers can target specific entity types (such as files, messages,
      events, sites, chats, people, and external items), apply filters, facets,
      and sorting, and even retrieve answers like bookmarks or Q&A, enabling
      tailored search experiences in custom apps, portals, or Teams.
  - aid: microsoft-graph:microsoft-graph-security
    name: Microsoft Graph Security
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/security-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Security is a unified set of APIs within Microsoft Graph
      that lets you access, correlate, and act on security data across Microsoft
      365 and integrated security solutions. It normalizes alerts and incidents
      from Microsoft Defender products and other providers, exposes security
      posture information such as Secure Score, and supports managing threat
      intelligence indicators. Developers use it to query and update
      alerts/incidents, automate response workflows, subscribe to change
      notifications, and integrate security insights into SIEM/SOAR tools and
      custom appsall through a consistent schema, single authentication and
      permissions model, and SDKs that simplify development.
  - aid: microsoft-graph:microsoft-graph-service-principals
    name: Microsoft Graph Service Principals
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/serviceprincipals-openapi-original.yml
        type: OpenAPI
    description: >-
      In Microsoft Entra ID (formerly Azure AD), a service principal is the
      identity an application uses to access resources, and the Microsoft Graph
      service principal is the tenant-local representation of the Microsoft
      Graph API itself. It publishes the set of OAuth 2.0 delegated scopes and
      application roles (permissions) that apps can request, and it is the
      target against which your apps own service principal is granted consent.
      Once consented, your app can obtain tokens and call Microsoft Grapheither
      on behalf of a user (delegated) or as an unattended daemon/background
      service (application). This model enables secure, least-privilege,
      auditable access to Microsoft 365 data and directory resources, using
      certificates or client secrets, governed by admin consent, Conditional
      Access, and directory policies.
  - aid: microsoft-graph:microsoft-graph-shares
    name: Microsoft Graph Shares
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/shares-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Shares is the part of Microsoft Graph that lets apps
      access a OneDrive or SharePoint item by its sharing link or token, without
      needing to know the site, drive, or item IDs. Given a share URL, you can
      resolve it to a sharedDriveItem and then work with the underlying
      driveItem or listItem: read metadata, navigate folder children, fetch
      thumbnails, and download contentand, if the link grants edit rights, make
      changes. It works across OneDrive (personal and business) and SharePoint,
      including anonymous links, by using an encoded form of the sharing URL
      (often the u! token) at the /shares/{shareIdOrUrl} endpoint. This is
      distinct from listing items shared with a user; Shares is specifically for
      dereferencing and operating on a single shared link in a uniform way.
  - aid: microsoft-graph:microsoft-graph-sites
    name: Microsoft Graph Sites
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/sites-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Sites is the Graph API surface for SharePoint Online,
      letting apps discover and work with sites and their content through a
      single, secure endpoint. It enables you to locate the root site or a site
      by URL, search for sites, and navigate a sites structure to access
      document libraries (drives), lists, list items, files, and modern site
      pages. You can read and update metadata, columns, and content types;
      follow or unfollow sites; work with the term store (taxonomy); and relate
      a site to connected resources like users, groups, and Teams. Because its
      part of Microsoft Graph, you get consistent authentication, granular
      permissions, and cross-service capabilities, plus change tracking and
      webhooks on supported resources to build reliable, automated content and
      intranet solutions.
  - aid: microsoft-graph:microsoft-graph-solutions
    name: Microsoft Graph Solutions
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/solutions-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph solutions connect apps to the data and intelligence across
      Microsoft 365 through a single, unified API. They enable secure access to
      users, groups, mail, calendars, files, Teams chats and meetings,
      SharePoint, OneDrive, Planner, devices, and security signals, so you can
      build experiences that personalize collaboration, automate workflows, and
      derive insights. With SDKs, webhooks and change notifications, delta
      queries, Graph Connectors, and Graph Data Connect, you can integrate
      external systems, react to changes in near real time, and run analytics at
      scaleall governed by Microsoft Entra IDs consent and granular
      permissions. The result is faster development, consistent security, and
      richer solutions embedded in Teams, Outlook, SharePoint, and custom
      lineofbusiness apps.
  - aid: microsoft-graph:microsoft-graph-storage
    name: Microsoft Graph Storage
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/storage-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph storage typically refers to the storage capabilities
      exposed through Microsoft Graphprimarily OneDrive and SharePointvia the
      Files and Drives APIs. It lets apps programmatically store and manage
      files and folders, upload and download (including large-file upload
      sessions), track changes with delta queries, generate thumbnails, search,
      and share content with rich permission controls. For app-specific data,
      developers can use the users OneDrive appFolder as a private per-app
      space, and attach custom metadata to Microsoft 365 entities using open or
      schema extensions. All of this is accessed through the Microsoft Graph
      REST API and SDKs with delegated or application permissions, inheriting
      Microsoft 365 security, compliance, and auditing.
  - aid: microsoft-graph:microsoft-graph-subscribed-skus
    name: Microsoft Graph Subscribed SKUs
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/subscribedskus-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Subscribed SKUs is the API/resource that lists the
      Microsoft 365/Azure AD license subscriptions your tenant owns. When you
      call GET /subscribedSkus, it returns each license plan (SKU) with its
      identifiers (skuId, skuPartNumber), seat counts (prepaidUnits and
      consumedUnits), subscription status (enabled, suspended, warning), and the
      included service plans. This lets apps and admins inventory licenses, map
      SKU IDs to human-readable plans, check capacity before assigning licenses,
      spot suspended or trial subscriptions, and build usage or compliance
      reports. In practice, you read subscribed SKUs to choose the right skuId,
      then use Graphs license assignment endpoints to add or remove that
      license for users or groups.
  - aid: microsoft-graph:microsoft-graph-subscriptions
    name: Microsoft Graph Subscriptions
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/subscriptions-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Subscriptions let your app receive near real-time change
      notifications (webhooks) when Microsoft 365 data changessuch as Outlook
      mail and calendar items, users and groups, files in OneDrive/SharePoint,
      or Teams chats and channels. You register a subscription that specifies
      the resource to watch and a publicly reachable HTTPS endpoint; Microsoft
      Graph validates the endpoint and then posts notifications whenever
      relevant items are created, updated, or deleted. Subscriptions are
      time-limited and must be renewed, and notifications include information
      your app can use to verify authenticity and correlate events. You can
      receive a lightweight payload and fetch details via Graph, or include
      encrypted resource data directly in the notification. This enables
      reactive apps, workflows, and sync processes that trigger immediately on
      changes across Microsoft 365.
  - aid: microsoft-graph:microsoft-graph-teams
    name: Microsoft Graph Teams
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/teams-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph for Teams exposes Microsoft Teams data and capabilities
      through a single, secure API so you can build integrations and automate
      Teams at scale. With it, you can create and manage teams, channels, chats,
      and memberships; post and read messages; schedule and manage meetings and
      webinars; access presence and call records; and install or configure Teams
      apps and tabs. It supports governance and lifecycle tasks such as
      provisioning, archiving, retention and export, policy application, and
      usage reporting. You can subscribe to change notifications for events like
      new messages or meeting updates, enabling real-time workflows. Available
      as REST endpoints and SDKs with delegated and app-only permissions, it
      respects Microsoft 365 security and compliance controls while letting you
      extend and tailor Teams experiences.
  - aid: microsoft-graph:microsoft-graph-teams-templates
    name: Microsoft Graph Teams Templates
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/teamstemplates-openapi-original.yml
        type: OpenAPI
    description: Needs a description
  - aid: microsoft-graph:microsoft-graph-teamwork
    name: Microsoft Graph Teamwork
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/teamwork-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Teamwork is the set of Microsoft Graph APIs that surface
      Microsoft Teams collaboration capabilities. It lets you programmatically
      create and manage teams and channels; add members and owners; read, post,
      and moderate chat and channel messages; install, configure, and manage
      Teams apps and tabs; work with frontline workforce features like
      schedules, shifts, and time off; use teamwork tags to target groups; send
      activity notifications; and discover a users associated teams. All of
      this is delivered with Graphs unified authentication, permissions,
      lifecycle management, and change notifications, so you can automate and
      integrate Teams experiences securely at scale.
  - aid: microsoft-graph:microsoft-graph-tenant-relationships
    name: Microsoft Graph Tenant Relationships
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/tenantrelationships-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Tenant Relationships is the part of the Microsoft Graph
      API that lets you model and manage how your Microsoft Entra ID tenant
      relates to other tenants. It provides endpoints to discover external
      tenants, create and govern delegated admin relationships (GDAP) between
      partners and customers, manage membership in a multi-tenant organization,
      and access managed tenants data used by Microsoft 365 Lighthouse. By
      centralizing these cross-tenant connections, it enables service providers
      and enterprises to automate onboarding, scope and assign permissions,
      monitor relationship status, and streamline operations and collaboration
      across many tenants in a consistent, policy-driven way.
  - aid: microsoft-graph:microsoft-graph-users
    name: Microsoft Graph Users
    tags:
      - Tag
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/users-openapi-original.yml
        type: OpenAPI
    description: >-
      Microsoft Graph Users refers to the Users resource in Microsoft Graph,
      which exposes Microsoft Entra ID (Azure AD) user accounts and their
      relationships and Microsoft 365 data through a unified API. It lets you
      list, read, create, update, and delete users; manage identities and
      lifecycle tasks such as assigning licenses, resetting passwords, and
      updating authentication settings; and retrieve related information like
      profile details, photos, managers, direct reports, group and role
      memberships. From a user, you can also navigate to their mail, calendar,
      OneDrive files, tasks, and Teams-related data. The endpoint supports
      powerful queries and change tracking via OData options like $select,
      $filter, $search, and delta, as well as batching for efficiency. Access
      requires OAuth 2.0 with delegated or application permissions, and many
      write or sensitive read operations need admin consent and least-privilege
      scopes.
name: Microsoft Graph
tags:
  - Productivity
  - Email
  - Contacts
  - Documents
  - Spreadsheets
  - Presentations
  - Tasks
  - T1
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    name: Portal
    type: Portal
  - url: https://developer.microsoft.com/en-us/graph/changelog/?showfilters=false
    name: Change Log
    type: ChangeLog
  - url: >-
      https://learn.microsoft.com/en-us/graph/sdks/sdks-overview?context=graph%2Fapi%2F1.0&view=graph-rest-1.0
    name: SDKs
    type: SDKs
  - url: >-
      https://learn.microsoft.com/en-us/graph/versioning-and-support?view=graph-rest-1.0
    name: Versioning
    type: Versioning
  - url: >-
      https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use?context=graph%2Fcontext&view=graph-rest-1.0
    name: Terms Of Service
    type: TermsOfService
  - url: >-
      https://learn.microsoft.com/en-us/graph/graph-explorer/graph-explorer-overview?view=graph-rest-1.0
    name: Getting Started
    type: GettingStarted
  - url: https://developer.microsoft.com/en-us/graph/graph-explorer
    name: Explorer
    type: Explorer
  - url: properties/v1.0
    name: OpenAPI
    type: OpenAPI
created: '2025-08-20'
modified: '2025-12-28'
position: Consumer
description: >-
  Microsoft Graph is the gateway to data and intelligence in Microsoft cloud
  services like Microsoft Entra and Microsoft 365. Use the wealth of data
  accessible through Microsoft Graph to build apps for organizations and
  consumers that interact with millions of users. 
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---