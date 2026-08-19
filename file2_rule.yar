rule file2_rule
{
    meta: 
        description = "This is rule for file2"
    
    strings:
        $str = "Malware_B_Signature"
        $hex = {4d 61 6c 77 61 72 65 5f 42}
    
    condition:
        $str and $hex
        and filesize == 512027          
}