rule file1_rule
{
    meta: 
        description = "This is rule for file1"
    
    strings:
        $str = "Malware_A_Signature"
        $hex = {4d 61 6c 77 61 72 65 5f 41}
    
    condition:
        $str and $hex      
}