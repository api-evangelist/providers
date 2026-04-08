---
aid: microsoft-windows-server
url: https://raw.githubusercontent.com/api-evangelist/microsoft-windows-server/refs/heads/main/apis.yml
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
  - type: OpenAPI
    url: https://docs.microsoft.com/rest/api/windows/
  - type: PowerShell Remoting
    url: https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/running-remote-commands
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
  - type: Specification
    url: https://www.dmtf.org/standards/ws-man
  - type: PowerShell Remoting FAQ
    url: https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/powershell-remoting-faq
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
  - type: PowerShell
    url: https://docs.microsoft.com/powershell/module/hyper-v/
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
  - type: GitHub
    url: https://github.com/Microsoft/windows-admin-center-sdk
  - type: Extension Development
    url: https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/developing-extensions
  - type: Gateway Plugin
    url: https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/develop-gateway-plugin
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
  - type: WMI
    url: https://docs.microsoft.com/previous-versions/windows/desktop/dnsprov/dns-wmi-provider
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
  - type: COM API Reference
    url: https://learn.microsoft.com/en-us/windows/win32/wmisdk/com-api-for-wmi
  - type: Scripting API Reference
    url: https://learn.microsoft.com/en-us/windows/win32/wmisdk/scripting-api-for-wmi
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
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/iis-administration/getting-started
  - type: GitHub
    url: https://github.com/microsoft/IIS.Administration
  - type: IIS Documentation
    url: https://learn.microsoft.com/en-us/iis/
  - type: OpenAPI
    url: openapi/iis-administration-api.yml
  - type: JSONSchema
    url: json-schema/microsoft-windows-server-site-schema.json
  - type: JSONLD
    url: json-ld/microsoft-windows-server-context.jsonld
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
  - type: API Reference
    url: https://learn.microsoft.com/en-us/windows/win32/termserv/terminal-services-api-reference
  - type: API Functions
    url: https://learn.microsoft.com/en-us/windows/win32/termserv/terminal-services-api-functions
  - type: Overview
    url: https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/overview
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
  - type: API Reference
    url: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/mscs/failover-cluster-apis-portal
  - type: PowerShell
    url: https://learn.microsoft.com/en-us/powershell/module/failoverclusters/
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
  - type: PowerShell
    url: https://learn.microsoft.com/en-us/powershell/module/dhcpserver/
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
  - type: SMB Management API
    url: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/smb/smb-management-api-portal
  - type: Protocol Specification
    url: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb/f210069c-7086-4dc2-885e-861d837df688
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
  - type: API Reference
    url: https://learn.microsoft.com/en-us/windows/win32/wes/windows-event-log-reference
  - type: Using Guide
    url: https://learn.microsoft.com/en-us/windows/win32/wes/using-windows-event-log
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
  - type: Deployment Guide
    url: https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/deploy-storage-spaces-direct
  - type: Storage Documentation
    url: https://learn.microsoft.com/en-gb/windows-server/storage/storage
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
  - type: RADIUS Server Planning
    url: https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-plan-server
name: Microsoft Windows Server
tags:
- Datacenter
- Enterprise
- Infrastructure
- Microsoft
- Operating System
- Server Management
- Windows Server
- Windows Server 2025
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and integration points for Microsoft Windows Server operating system including management, networking, storage, virtualization, security, and remote administration capabilities for enterprise server infrastructure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

