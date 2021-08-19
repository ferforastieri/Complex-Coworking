# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class LDAPSyncConfig(AppConfig):
    name = 'ldap_sync'

    def ready(self):
        # Load and connect signal recievers
        import ldap_sync.signals


# Copyright 2021 Office Nomads LLC (https://officenomads.com/) Licensed under the AGPL License, Version 3.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at https://www.gnu.org/licenses/agpl-3.0.html. Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
