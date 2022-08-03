from .....rust import Enum, Struct, Tuple, Dict
Event = Enum[("Peer", "iroha_data_model.events.data.events.peer.PeerEvent"), ("Domain", "iroha_data_model.events.data.events.domain.DomainEvent"), ("Account", "iroha_data_model.events.data.events.account.AccountEvent"), ("AssetDefinition", "iroha_data_model.events.data.events.asset.AssetDefinitionEvent"), ("Asset", "iroha_data_model.events.data.events.asset.AssetEvent"), ("Trigger", "iroha_data_model.events.data.events.trigger.TriggerEvent"), ("Role", "iroha_data_model.events.data.events.role.RoleEvent")] 