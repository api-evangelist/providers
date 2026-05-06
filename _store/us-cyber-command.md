---
aid: us-cyber-command
url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/apis.yml
apis:
  - aid: us-cyber-command:cnmf-virustotal-malware-sharing
    name: CNMF Malware Sharing via VirusTotal
    tags:
      - Cybersecurity
      - Malware
      - Threat Intelligence
      - VirusTotal
      - Federal Government
    humanURL: https://www.virustotal.com/gui/user/CYBERCOM_Malware_Alert/comments
    properties:
      - url: https://www.virustotal.com/gui/user/CYBERCOM_Malware_Alert/comments
        type: Documentation
        title: CYBERCOM VirusTotal Malware Alert Feed
      - url: https://www.cybercom.mil/Media/News/News-Display/Article/1681533/new-cnmf-initiative-shares-malware-samples-with-cybersecurity-industry/
        type: GettingStarted
        title: CNMF Malware Sharing Initiative Announcement
      - url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/json-schema/uscybercom-malware-sample-schema.json
        type: JSONSchema
        title: Malware Sample Schema
      - url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/json-schema/uscybercom-threat-actor-schema.json
        type: JSONSchema
        title: Threat Actor Schema
    description: The U.S. Cyber Command Cyber National Mission Force (CNMF) shares unclassified malware samples on VirusTotal via the CYBERCOM_Malware_Alert account. This public threat intelligence sharing program posts malware samples attributed to state-sponsored threat actors from Russia, Iran, North Korea, and other adversaries. The program launched in November 2018 to improve global cybersecurity by sharing samples with the security community. Follow @CNMF_VirusAlert on Twitter/X for alerts on new uploads.
  - aid: us-cyber-command:uscybercom-news-media
    name: USCYBERCOM News and Advisories
    tags:
      - Cybersecurity
      - Federal Government
      - Military
      - Advisories
    humanURL: https://www.cybercom.mil/Media/News/
    properties:
      - url: https://www.cybercom.mil/Media/News/
        type: Documentation
        title: USCYBERCOM News and Press Releases
      - url: https://www.cybercom.mil/Portals/56/Documents/Cyber%20Command%20Problem%20Set%203rd%20Edition.pdf
        type: Documentation
        title: Cyber Command Challenge Problems Guidance
      - url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/json-schema/uscybercom-advisory-schema.json
        type: JSONSchema
        title: Cybersecurity Advisory Schema
    description: Public news releases, advisories, and operational announcements from U.S. Cyber Command. Includes joint cybersecurity advisories, malware disclosure announcements, defensive cyber operations public statements, and the Cyber Command Challenge Problems guidance for industry collaboration.
name: US Cyber Command
tags:
  - Cybersecurity
  - Federal Government
  - Military
  - Threat Intelligence
  - Defense
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-25'
modified: '2026-05-03'
position: Consumer
description: US Cyber Command (USCYBERCOM) is a Unified Combatant Command of the United States Armed Forces responsible for directing, synchronizing, and coordinating cyberspace operations. It defends Department of Defense information networks and prepares to conduct full spectrum military cyberspace operations to ensure freedom of action in cyberspace and deny the same to adversaries. USCYBERCOM's Cyber National Mission Force (CNMF) publicly shares unclassified malware samples attributed to state-sponsored threat actors via VirusTotal, contributing to the global cybersecurity community's threat intelligence capabilities. USCYBERCOM also collaborates with CISA, NSA, and allied nations on joint cybersecurity advisories and threat disclosures.
common:
  - type: Website
    url: https://www.cybercom.mil/
  - type: Documentation
    url: https://www.cybercom.mil/Media/News/
    title: News and Advisories
  - type: Contact
    url: https://www.cybercom.mil/About/Contact/
    title: Contact USCYBERCOM
  - type: Features
    data:
      - name: CNMF Malware Sharing Program
        description: The Cyber National Mission Force (CNMF) shares unclassified malware samples on VirusTotal (CYBERCOM_Malware_Alert) attributed to state-sponsored threat actors from Russia, Iran, North Korea, and other adversaries.
      - name: Joint Cybersecurity Advisories
        description: USCYBERCOM publishes joint cybersecurity advisories with CISA, NSA, FBI, and allied nation cybersecurity agencies on active threats and recommended mitigations.
      - name: Defensive Cyber Operations
        description: USCYBERCOM conducts defensive cyber operations to detect and respond to malicious cyber activity targeting U.S. and partner networks, sharing findings through public disclosures.
      - name: Cyber Command Challenge Problems
        description: Published guidance identifying high-priority cybersecurity challenge problems for industry, academia, and government collaboration to advance national cyber defense capabilities.
      - name: Hunt Forward Operations
        description: At partner nation invitation, USCYBERCOM deploys hunt forward teams to identify malicious cyber activity on allied networks, with findings sometimes shared publicly via VirusTotal.
  - type: UseCases
    data:
      - name: Threat Intelligence Enrichment
        description: Security analysts and threat hunters use CNMF VirusTotal uploads to identify and analyze state-sponsored malware, updating detection rules and IOC databases.
      - name: Malware Analysis and Attribution
        description: Security researchers analyze USCYBERCOM-disclosed malware samples to understand adversary TTPs, develop detection signatures, and support attribution analysis.
      - name: Cybersecurity Advisory Tracking
        description: Organizations and security teams track USCYBERCOM joint advisories to understand active threats and implement recommended mitigations.
      - name: Defensive Tool Development
        description: Security tool developers use CNMF malware samples to test and improve detection capabilities, antivirus signatures, and threat hunting tools.
      - name: Government Threat Awareness
        description: Government agencies and critical infrastructure operators monitor USCYBERCOM disclosures for nation-state threat indicators relevant to their networks.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/vocabulary/us-cyber-command-vocabulary.yml
    title: US Cyber Command Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/us-cyber-command/refs/heads/main/json-ld/us-cyber-command-context.jsonld
    title: US Cyber Command JSON-LD Context
  - type: Integrations
    data:
      - name: VirusTotal
        description: CNMF publishes malware samples to VirusTotal via the CYBERCOM_Malware_Alert account for public analysis and sharing.
      - name: CISA (Cybersecurity and Infrastructure Security Agency)
        description: USCYBERCOM collaborates with CISA on joint cybersecurity advisories, malware disclosures, and critical infrastructure defense.
      - name: NSA Cybersecurity Directorate
        description: USCYBERCOM and NSA coordinate on threat intelligence sharing and jointly author cybersecurity advisories on nation-state threats.
      - name: Five Eyes Alliance
        description: USCYBERCOM partners with UK NCSC, Canadian CCCS, Australian ACSC, and New Zealand NCSC for joint threat intelligence and advisory publications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
