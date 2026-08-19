rule file3_rule
{
    meta: 
        description = "This is rule for file3"
    
    strings:
        $str = "Malware_C_Signature"
        $hex = {4d 61 6c 77 61 72 65 5f 43}
    
    condition:
        $str and $hex          
}