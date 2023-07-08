def create_response(success, data=None, item=None, items=None,
                    err_name="Operation Failed", err_message=None):
    if success:
        if data is not None:
            return {
                'success': True,
                'data': data,
            }
        elif item is not None:
            return {
                'success': True,
                'data': {
                    'item': item
                }
            }
        elif items is not None:
            return {
                'success': True,
                'data': {
                    'items': items
                }
            }
    else:
        return{
            'success': False,
            'error': {
                'name': err_name,
                'message': err_message
            }
        }
