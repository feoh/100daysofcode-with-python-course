import wmi

running_windows_processes = {}

wmi = wmi.WMI()
processes = wmi.Win32_Process()

running_windows_processes = [
    {'Id': process.ProcessId, 'CreationDate': process.CreationDate, 'Description': process.Description,
     'Name': process.Name} for process in processes]
