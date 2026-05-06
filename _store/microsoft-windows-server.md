---
aid: microsoft-windows-server
name: Microsoft Windows Server
description: APIs and integration points for Microsoft Windows Server operating system including management, networking, storage, virtualization, security, and remote administration capabilities for enterprise server infrastructure.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.microsoft.com/windows-server
tags:
  - Datacenter
  - Enterprise
  - Infrastructure
  - Microsoft
  - Operating System
  - Server Management
  - Windows Server
  - Windows Server 2025
created: '2024'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - name: Windows Server Management API
    description: PowerShell and WMI-based management APIs for Windows Server administration.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://docs.microsoft.com/windows-server/administration/
    baseURL: https://localhost
    tags:
      - Administration
      - Management
      - PowerShell
      - WMI
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/powershell/windows/get-started
    contact:
      - FN: Microsoft Support
        email: support@microsoft.com
        url: https://support.microsoft.com
  - name: Windows Remote Management (WinRM)
    description: WS-Management protocol implementation for remote management of Windows servers using SOAP-based web services for configuration and operations.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://docs.microsoft.com/windows/win32/winrm/portal
    baseURL: http://localhost:5985
    tags:
      - PowerShell Remoting
      - Remote Management
      - SOAP
      - WS-Management
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/windows/win32/winrm/windows-remote-management-portal
  - name: Active Directory Domain Services API
    description: LDAP and REST APIs for Active Directory management and authentication.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://docs.microsoft.com/windows-server/identity/ad-ds/
    baseURL: ldap://localhost:389
    tags:
      - Active Directory
      - Authentication
      - Directory Services
      - LDAP
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/windows/win32/ad/active-directory-domain-services
      - type: SDK
        url: https://docs.microsoft.com/dotnet/api/system.directoryservices
  - name: Hyper-V Management API
    description: APIs for managing Hyper-V virtualization platform including virtual machines, virtual switches, and virtual storage.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://docs.microsoft.com/virtualization/hyper-v-on-windows/
    baseURL: https://localhost
    tags:
      - Hyper-V
      - Virtual Machines
      - Virtualization
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/virtualization/api/
  - name: Windows Server Update Services (WSUS) API
    description: APIs for managing Windows updates across enterprise environments.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://docs.microsoft.com/windows-server/administration/windows-server-update-services/
    baseURL: https://localhost:8530
    tags:
      - Patch Management
      - Updates
      - WSUS
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/previous-versions/windows/desktop/aa354519(v=vs.85)
      - type: SDK
        url: https://docs.microsoft.com/dotnet/api/microsoft.updateservices.administration
  - name: Windows Admin Center API
    description: Modern web-based management interface REST API for Windows Server that provides a gateway service for relaying commands and scripts to managed nodes.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://docs.microsoft.com/windows-server/manage/windows-admin-center/
    baseURL: https://localhost:6516
    tags:
      - Admin Center
      - Gateway
      - REST API
      - Web Management
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/windows-server/manage/windows-admin-center/extend/extensibility-overview
      - type: GitHubRepository
        url: https://github.com/Microsoft/windows-admin-center-sdk
  - name: DNS Server Management API
    description: APIs for managing Windows DNS Server services.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://docs.microsoft.com/windows-server/networking/dns/
    baseURL: https://localhost
    tags:
      - DNS
      - Name Resolution
      - Networking
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/powershell/module/dnsserver/
  - name: Windows Management Instrumentation (WMI) API
    description: Infrastructure for management data and operations on Windows-based operating systems providing COM, scripting, and .NET APIs for system administration and monitoring.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page
    baseURL: https://localhost
    tags:
      - COM
      - Management
      - Monitoring
      - Scripting
      - WMI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page
      - type: APIReference
        url: https://learn.microsoft.com/en-us/windows/win32/wmisdk/com-api-for-wmi
  - name: IIS Administration API
    description: REST API for managing Internet Information Services (IIS) web servers that enables configuration and monitoring from any HTTP client.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/iis-administration/
    baseURL: https://localhost:55539
    tags:
      - IIS
      - REST API
      - Web Management
      - Web Server
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/iis-administration/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/iis-administration/getting-started
      - type: GitHubRepository
        url: https://github.com/microsoft/IIS.Administration
      - type: OpenAPI
        url: openapi/iis-administration-api.yml
  - name: Remote Desktop Services API
    description: Win32 API for managing Remote Desktop Services including session management, virtual channels, user configuration, and the Remote Desktop Protocol.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/win32/termserv/terminal-services-portal
    baseURL: https://localhost
    tags:
      - RDS
      - Remote Access
      - Remote Desktop
      - Terminal Services
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/win32/termserv/terminal-services-portal
      - type: APIReference
        url: https://learn.microsoft.com/en-us/windows/win32/termserv/terminal-services-api-reference
  - name: Failover Clustering API
    description: APIs for defining and managing software and hardware components on failover clusters to increase application scalability and availability.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview
    baseURL: https://localhost
    tags:
      - Cluster Management
      - Failover Clustering
      - High Availability
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/mscs/failover-cluster-apis-portal
  - name: DHCP Server Management API
    description: APIs and PowerShell cmdlets for managing Dynamic Host Configuration Protocol server services including leases, reservations, and scopes.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-deploy-wps
    baseURL: https://localhost
    tags:
      - DHCP
      - IP Address Management
      - Networking
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/dhcp/dhcp-server-management-api
  - name: SMB File Server API
    description: Server Message Block protocol APIs and WMI management classes for managing file shares, share access, and network file sharing across Windows Server environments.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview
    baseURL: https://localhost
    tags:
      - File Sharing
      - Network Storage
      - SMB
      - Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview
  - name: Windows Event Log API
    description: API for instrumenting, querying, and consuming event logs on Windows Server for diagnostics, monitoring, and auditing.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows/win32/wes/windows-event-log
    baseURL: https://localhost
    tags:
      - Diagnostics
      - Event Log
      - Logging
      - Monitoring
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/win32/wes/windows-event-log
      - type: APIReference
        url: https://learn.microsoft.com/en-us/windows/win32/wes/windows-event-log-reference
  - name: Storage Spaces Direct API
    description: APIs and PowerShell management for software-defined storage enabling clustering of servers with internal storage for hyper-converged infrastructure.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/storage-spaces-direct-overview
    baseURL: https://localhost
    tags:
      - Hyper-Converged
      - Software-Defined Storage
      - Storage
      - Storage Spaces Direct
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/storage-spaces-direct-overview
  - name: Network Policy Server (NPS) RADIUS API
    description: Network Policy Server providing centralized RADIUS authentication, authorization, and accounting for wireless, VPN, and dial-up connections.
    image: https://www.microsoft.com/favicon.ico
    humanURL: https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top
    baseURL: https://localhost
    tags:
      - Authentication
      - Network Access
      - NPS
      - RADIUS
      - VPN
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://docs.microsoft.com/windows-server/
  - type: Support
    url: https://support.microsoft.com/windows-server
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/windows-server/bg-p/WindowsServer
  - type: TermsOfService
    url: https://www.microsoft.com/licensing/terms/
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/privacystatement
  - type: GitHubRepository
    url: https://github.com/MicrosoftDocs/windowsserverdocs
  - type: Security
    url: https://learn.microsoft.com/en-us/windows-server/security/tls/tls-ssl-schannel-ssp-overview
  - type: Features
    data:
      - name: Web Server Management
        description: REST API for managing IIS web sites, applications, and application pools with full CRUD operations and configuration management.
      - name: Active Directory Services
        description: LDAP and API-based management of directory services, user authentication, group policies, and domain controllers.
      - name: Hyper-V Virtualization
        description: Create, manage, and monitor virtual machines, virtual switches, and storage with PowerShell and WMI APIs.
      - name: Remote Server Administration
        description: Manage servers remotely through WinRM, PowerShell Remoting, Windows Admin Center, and Remote Desktop Services.
      - name: Failover Clustering
        description: High availability clustering with automatic failover for critical workloads including SQL Server, Hyper-V, and file servers.
      - name: Software-Defined Storage
        description: Storage Spaces Direct for hyper-converged infrastructure with pool management, tiering, and resilient storage volumes.
      - name: DNS and DHCP Services
        description: Network infrastructure services with APIs for DNS zone management and DHCP scope configuration.
      - name: Security and Compliance
        description: RADIUS authentication via NPS, TLS/SSL management, Windows Event Log auditing, and security policy enforcement.
  - type: UseCases
    data:
      - name: Enterprise Web Hosting
        description: Deploy and manage web applications on IIS with automated site provisioning, SSL certificate management, and application pool isolation.
      - name: Infrastructure Automation
        description: Automate server provisioning, configuration management, and patch deployment using PowerShell, WMI, and REST APIs.
      - name: Hybrid Cloud Management
        description: Manage on-premises Windows Server infrastructure alongside Azure resources through Windows Admin Center and Azure Arc.
      - name: Virtual Desktop Infrastructure
        description: Deploy and manage Remote Desktop Services for virtual desktop and application delivery to remote workers.
      - name: High Availability Deployments
        description: Configure failover clustering and storage replication for mission-critical applications requiring zero downtime.
  - type: Integrations
    data:
      - name: Microsoft Azure
        description: Extend on-premises Windows Server to Azure with Azure Arc, Azure Backup, Azure Site Recovery, and hybrid networking.
      - name: System Center
        description: Enterprise management with System Center Configuration Manager, Operations Manager, and Virtual Machine Manager.
      - name: Microsoft Defender
        description: Integrated security with Microsoft Defender for Servers, threat detection, and vulnerability management.
      - name: Active Directory Federation Services
        description: Enable single sign-on and federated identity across on-premises and cloud applications with ADFS.
      - name: Azure Monitor
        description: Collect and analyze Windows Server performance metrics, logs, and diagnostics in Azure Monitor.
  - type: NaftikoCapability
    url: capabilities/web-server-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
