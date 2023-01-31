clear

%visadevlist
obj1 = visadev("USB0::0x2A8D::0x2F01::MY54412848::0::INSTR");

%type = write(obj1, ':FUNCtion:IMPedance:TYPE?');

write(obj1, ':FUNCtion:IMPedance:TYPE CPRP');%%RD|CPQ|CPG|CPRP|CSD|CSQ|CSRS|LPD|LPQ|LPG|LPRP|LPRD|LSD|LSQ|LSRS|LS
%%RD|RX|ZTD|ZTR|GB|YTD|YTR|VDID
write(obj1, ':FREQuency:CW 10000');
write(obj1, ':VOLTage:LEVel 20');
write(obj1, ':APERture SHORt');%SHORt MEDium
write(obj1, ':DISPlay:ENABle 1');%disable display


y = [];
times = [];
tic
while toc < 350
    readout = writeread(obj1, "FETCh:IMPedance:CORRected?");
    %readout = writeread(obj1, "FETCh:IMPedance:FORMatted?");
    readout = split(readout,",");
    y1 = eval(readout(1));
    y2 = eval(readout(2));
    y = [y;[y1,y2]];
    times = [times; toc];
end

save("calibrate.mat","y","times");
