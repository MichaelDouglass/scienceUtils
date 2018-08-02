FOR /L %%A in (1,1,256) DO (
    arp -a 192.168.1.%%A >> C:\Users\Folio\Desktop\MAC_Log.log
)
type MAC_Log.log | findstr /v ARP | findstr /v Interface > C:\Users\Folio\Desktop\MacLog20180731_1000.txt
pause