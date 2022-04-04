# HeaderInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Block/header ID | 
**parent_id** | **str** | ID of the parental block/header | 
**version** | **int** | Version of the header | 
**height** | **int** | Block/header height | 
**epoch** | **int** | Block/header epoch (Epochs are enumerated from 0) | 
**difficulty** | **str** | Block/header difficulty | 
**ad_proofs_root** | **str** | Hex-encoded root of the corresponding AD proofs | 
**state_root** | **str** | Hex-encoded root of the corresponding state | 
**transactions_root** | **str** | Hex-encoded root of the corresponding transactions | 
**timestamp** | **int** | Timestamp the block/header was created | 
**n_bits** | **int** | Encoded required difficulty | 
**size** | **int** | Size of the header in bytes | 
**extension_hash** | **str** | Hex-encoded hash of the corresponding extension | 
**pow_solutions** | [**PowSolutionInfo**](PowSolutionInfo.md) |  | 
**votes** | [**Tuple3ByteByteByte**](Tuple3ByteByteByte.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

